__author__ = 'jcranwellward'

import os
import json
import requests
import datetime

from django.conf import settings
from django.template.defaultfilters import slugify

from requests.auth import HTTPBasicAuth
from pymongo import MongoClient

from EquiTrack.celery import app


supplies = MongoClient(settings.MONGODB_URL)[settings.MONGODB_DATABASE]


@app.task
def send(message):
    if settings.SLACK_URL:
        requests.post(
            settings.SLACK_URL,
            data=json.dumps({'text': message})
        )


def set_docs(docs):

    payload_json = json.dumps(
        {
            'docs': docs,
            'all_or_nothing': True
        }
    )
    response = requests.post(
        os.path.join(settings.COUCHBASE_URL, '_bulk_docs'),
        headers={'content-type': 'application/json'},
        auth=HTTPBasicAuth(settings.COUCHBASE_USER, settings.COUCHBASE_PASS),
        data=payload_json,
    )
    return response


def set_unisupply_user(username, password):

    user_docs = []
    user_docs.append(
        {
            "_id": username,
            "type": "user",
            "username": username,
            "password": password,
            "organisation": username,
        }
    )

    set_docs.delay(user_docs)


@app.task
def set_unisupply_distribution(distribution_plan):

        response = set_docs([
            {
                "_id": slugify("{} {} {} {}".format(
                    distribution_plan.partnership,
                    distribution_plan.item,
                    distribution_plan.location,
                    distribution_plan.quantity
                )),
                "partner_name": distribution_plan.partnership.partner.name,
                "assessment_type": "institution",
                "criticality": "0",
                "item_list": [
                    {
                        "item_id": "SB001",
                        "item_type": distribution_plan.item.name,
                        "quantity": distribution_plan.quantity
                    }
                ],
                "location": {
                    "location_type": distribution_plan.location.gateway.name,
                    "p_code": distribution_plan.location.p_code,
                    "p_code_name": distribution_plan.location.name,
                },
                "type": "assessment",
                "completed": False,
                "creation_date": datetime.datetime.now().isoformat(),
                "name": "N/A",
            }
        ])
        if response.status_code in [requests.codes.ok, requests.codes.created]:
            distribution_plan.send = False
            distribution_plan.sent = True
            distribution_plan.save()

        return response.text


def import_docs(**kwargs):
    """
    Imports docs from couch base
    """
    data = requests.get(
        os.path.join(settings.COUCHBASE_URL, '_all_docs'),
        auth=HTTPBasicAuth(settings.COUCHBASE_USER, settings.COUCHBASE_PASS)
    ).json()

    existing = supplies.data.find(**kwargs).count()
    for row in data['rows']:
        doc = row['doc']
        supplies.data.update({'_id': doc['_id']}, doc, upsert=True)

    imported = supplies.data.find(**kwargs).count()

    send('Import finished: '
         '{} new assessments, '
         'total now {}'.format(
         imported - existing,
         imported,
    ))

