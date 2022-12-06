import time

from behave import *


@given(u'Opened HomePage website')
def step_impl(context):
    context.begin_home_page.go_home()


# ----------- Search with empty field & Search with valid input field
@When("Click on the '{field}' input field.")
def step_impl(context, field):
    context.begin_home_page.click_input_search_field(field)


@when(u"Enter in '{field}' valid '{value}' parameters.")
def step_impl(context, field, value):
    context.begin_home_page.input_data(field, value)


@then(u'Search button is not displayed.')
def step_impl(context):
    assert context.begin_home_page.button_status() is False  # aici de modificat cu is


@then(u'Search button is displayed.')
def step_impl(context):
    assert context.begin_home_page.button_status() is True


# ---------Click nav-bar buttons
@when(u'Click the "{button}".')
def step_impl(context, button):
    context.begin_home_page.go_to(button)


@then(u'The page with "{url}" is opened.')
def step_impl(context, url):
    expected_url = "https://magento.softwaretestingboard.com/" + url
    assert context.browser.get_current_url() == expected_url


# ----------Functionality of products
@when(u'Scroll down on the page.')
def step_impl(context):
    context.browser.scroll_down(1800)


@when(u'Click on the "{color}".')
def step_impl(context, color):
    context.begin_home_page.color_selector(color)


@when(u'Click the "{measure}" measure.')
def step_impl(context, measure):
    context.begin_home_page.measure_selector(measure)


@when(u'Click on the "{action}" action.')
def step_impl(context, action):
    context.begin_home_page.action_selector(action)
    time.sleep(3)


# ------------Send invalid/valid Email Subscription
@when(u"Enter in '{field}' valid \'\' parameters.")
def step_impl(context, field, value=''):
    context.begin_home_page.input_data(field, value)


@when(u'Scroll down on the footer of the page.')
def step_impl(context):
    context.browser.scroll_down(2500)


@then(u"Check the '{message}'.")
def step_impl(context, message):
    message_expect = message
    assert context.begin_home_page.check_message(message) == message_expect


@then(u'Check the \'\'.')
def step_impl(context, message=''):
    assert context.begin_home_page.check_message(message) == ''
