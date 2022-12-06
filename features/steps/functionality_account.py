import time

from behave import *


@When('Click the "{field}" from my cart.')
def step_impl(context, field):
    context.browser.click_item_id(field)
    time.sleep(2)


@When('Scroll up on the page.')
def step_impl(context):
    context.browser.scroll_up()


@Then('Click "{value}" submit.')
def step_impl(context, value):
    time.sleep(4)
    context.browser.click_item_xpath(value)


@when('The page redirect to the "{expected_page}" page.')
def step_impl(context, expected_page):
    expected_url = "https://magento.softwaretestingboard.com/" + expected_page
    assert context.browser.get_current_url() == expected_url


@when('Hover on the "{value}" button.')
def step_impl(context, value):
    context.functionality_account.hover_button(value)


@then('The message contain "{message}".')
def step_impl(context, message):
    assert context.functionality_account.check_contain(message) is True
