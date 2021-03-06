__author__ = 'unicef-leb-inn'

from rest_framework import viewsets, mixins, permissions
from rest_framework.generics import ListAPIView

from .models import CartoDBTable, GatewayType, Location
from .serializers import (
    CartoDBTableSerializer,
    GatewayTypeSerializer,
    LocationSerializer,
)


class CartoDBTablesView(ListAPIView):
    """
    Gets a list of CartoDB tables for the mapping system
    """
    queryset = CartoDBTable.objects.all()
    serializer_class = CartoDBTableSerializer
    permission_classes = (permissions.IsAdminUser,)


class LocationTypesViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """
    Returns a list off all Location types
    """
    queryset = GatewayType.objects.all()
    serializer_class = GatewayTypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class LocationsViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """
    Returns a list of all Locations
    """
    lookup_field = 'p_code'
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = super(LocationsViewSet, self).get_queryset()
        p_code = self.kwargs.get('p_code')
        if p_code:
            return queryset.filter(p_code=p_code)
        return queryset


class LocationQuerySetView(ListAPIView):
    model = Location
    lookup_field = 'q'
    serializer_class = LocationSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        qs = self.model.objects
        if q:
            qs = qs.filter(name__icontains=q)

        # return maximum 7 records
        return qs.all()[:7]