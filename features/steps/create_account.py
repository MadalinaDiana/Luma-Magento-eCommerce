from behave import *


@given(u'Opened the Create account page.')
def step_impl(context):
    context.create_account.go_home()


@when('Enter invalid/valid "{firstname}","{lastname}","{email}","{password}" and "{confpassword}" input.')
def step_impl(context, firstname, lastname, email, password, confpassword):
    context.create_account.enter_values(firstname, lastname, email, password, confpassword)


@When("Click submit button.")
def step_impl(context):
    context.create_account.click_submit()