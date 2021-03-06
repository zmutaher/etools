from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

@given('launch UniSupply app')
def step_impl(context):
    try:
        # driver = context.browser
        context.util.screenshot('UniSupply app')

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('tap on the link for First Time users')
def step_impl(context):
    try:
        driver = context.browser

        driver.find_element_by_id("button_settings").click()
        # context.util.screenshot("First Time users")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('press the plus button')
def step_impl(context):
    try:
        driver = context.browser
        context.util.screenshot("First Time users")
        driver.find_element_by_id("addButton").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you will be asked to name your preference setting to proceed. Type any name')
def step_impl(context):
    try:
        driver = context.browser
        context.util.screenshot("Preference settings name")
        driver.find_element_by_id("editTextDialogUserInput").send_keys("DEMO 1")
        driver.find_element_by_id('button1').click()

        driver.implicitly_wait(15)
        # context.util.screenshot("Preference settings list")

        driver.implicitly_wait(15)
    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('enter in the following details in the fields provided')
def step_impl(context):
    try:
        driver = context.browser
        util = context.util
        driver.implicitly_wait(15)

        driver.find_element_by_link_text("Server Base URL:").click()
        driver.find_element_by_id("edit").send_keys(util.read_config("app_server_baseurl"))
        driver.find_element_by_id("button1").click()

        driver.find_element_by_link_text("Server Port:").click()
        driver.find_element_by_id("edit").send_keys(util.read_config("app_server_port"))
        driver.find_element_by_id("button1").click()

        driver.find_element_by_link_text("Database Instance Name:").click()
        driver.find_element_by_id("edit").send_keys(util.read_config("app_database_name"))
        driver.find_element_by_id("button1").click()

        driver.find_element_by_link_text("Server Username:").click()
        driver.find_element_by_id("edit").send_keys(util.read_config("app_server_username"))
        driver.find_element_by_id("button1").click()

        driver.find_element_by_link_text("Server Password:").click()
        driver.find_element_by_id("edit").send_keys(util.read_config("app_server_password"))
        driver.find_element_by_id("button1").click()

        context.util.screenshot("Preference settings details")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@when('tap "Switch Environment"')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("switchWidget").click()
        driver.implicitly_wait(30)
        context.util.screenshot("Switch Environment")
        driver.implicitly_wait(30)

        driver.find_element_by_link_text("Initialise Database for DEMO_1").click()
    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you should now see your preference name in the list')
def step_impl(context):
    try:
        driver = context.browser
        driver.implicitly_wait(10)
        context.util.screenshot("preference name in the list")
        driver.find_element_by_id("action_bar_title").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('tap "UniSupply" to return to login screen')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("action_bar_title").click()
        context.util.screenshot("return to login screen")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@given('login into UniSupply with the credentials provided by your UNICEF focal point "{username}" and "{password}"')
def step_impl(context, username, password):
    try:
        driver = context.browser

        driver.find_element_by_id("editText_username").click()
        driver.find_element_by_id("editText_username").clear()
        driver.find_element_by_id("editText_username").send_keys(username)
        driver.find_element_by_id("editText_password").click()
        driver.find_element_by_id("editText_password").clear()
        driver.find_element_by_id("editText_password").send_keys(password)

        chain = ActionChains(driver)
        """ Send search key"""
        chain.send_keys(u'\uE007').perform()

        context.util.screenshot("login into UniSupply")
        driver.find_element_by_id("button_login").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you will see a list of all distributions by district and supply type')
def step_impl(context):
    try:
        driver = context.browser
        # driver.implicitly_wait(100)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        context.util.screenshot("all distributions by district and supply type")
        driver.find_element_by_id("doc_name").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('tap on any district name to see the distribution details')
def step_impl(context):
    try:
        driver = context.browser
        driver.implicitly_wait(50)
        context.util.screenshot("distribution details")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@when('you tap on the item name to record the quantities distributed in this location')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("doc_name").click()
        context.util.screenshot("quantities distributed in this location")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you can scroll up through the numbers')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("numberpicker_input").send_keys(8)
        driver.implicitly_wait(10)
        context.util.screenshot("scroll up through the numbers")


    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you type a number into the number field')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("numberpicker_input").send_keys(2500)
        driver.implicitly_wait(10)
        context.util.screenshot("select total number")
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("Done").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you can click on "Complete All" to record all quantities distributed')
def step_impl(context):
    try:
        driver = context.browser
        driver.implicitly_wait(10)
        # driver.find_element_by_id("doc_name").click()
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "completeall")))
        # driver.find_element_by_id("completeall").click()
        # driver.implicitly_wait(10)
        # context.util.screenshot("Complete all")
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("Done").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('press "done" to return to the district details screen')
def step_impl(context):
    try:
        driver = context.browser
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Done")))
        driver.find_element_by_id("Done").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('you will see that the district details have updated')
def step_impl(context):
    try:
        driver = context.browser
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "button_done")))
        context.util.screenshot("back to updated district details")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('press "done" to return to the main screen')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("button_done").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('the overview and reports screens will also reflect delivery status')
def step_impl(context):
    try:
        driver = context.browser
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        context.util.screenshot("back to main screen")

        driver.find_element_by_link_text("Reports").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        driver.find_element_by_id("doc_name").click()
        context.util.screenshot("reports screens reflect the partial delivery")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('continue updating deliveries as necessary')
def step_impl(context):
    try:
        driver = context.browser


    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@when('all items for one district have been completed')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_link_text("Finished").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        context.util.screenshot("finished items")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('the item will be moved from the "started" tab into the "finished" tab')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_link_text("Started").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        driver.find_element_by_id("doc_name").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('to move a distribution to the "finished" tab manually')
def step_impl(context):
    try:
        driver = context.browser


    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('tap the "Force Completion" button on a distribution')
def step_impl(context):
    try:
        driver = context.browser
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button_forceComplete")))
        driver.find_element_by_id("button_forceComplete").click()
        driver.find_element_by_id("button_done").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        driver.find_element_by_link_text("Finished").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doc_name")))
        context.util.screenshot("manually moved to finished")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('to ensure that distributions are synced with the eTools system.Go to the "Sync" tab')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_link_text("Sync").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button_forceSync")))
        context.util.screenshot("Force Sync")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)


@then('tap "Force Sync"')
def step_impl(context):
    try:
        driver = context.browser
        driver.find_element_by_id("button_forceSync").click()
        context.util.screenshot("Sync forced")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)

@then('sign out from UniSupply')
def step_impl(context):
    try:
        driver = context.browser
        driver.implicitly_wait(50)

        driver.find_element_by_xpath("//ActionMenuView").click()
        # driver.find_element_by_id("action_bar").click()
        driver.find_element_by_id("action_signout")

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)

@then('login into UniSupply "{username}" and "{password}"')
def step_impl(context, username, password):
    try:
        driver = context.browser

        driver.find_element_by_id("editText_username").click()
        driver.find_element_by_id("editText_username").clear()
        driver.find_element_by_id("editText_username").send_keys(username)
        driver.find_element_by_id("editText_password").click()
        driver.find_element_by_id("editText_password").clear()
        driver.find_element_by_id("editText_password").send_keys(password)

        chain = ActionChains(driver)
        """ Send search key"""
        chain.send_keys(u'\uE007').perform()

        context.util.screenshot("login into UniSupply")
        driver.find_element_by_id("button_login").click()

    except Exception as ex:
        context.util.screenshot_error()
        raise Exception(ex)