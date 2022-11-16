from behave import *

use_step_matcher("re")


@given('we are at "https://www\.epam\.com/about/who-we-are/contact"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we are at "https://www.epam.com/about/who-we-are/contact"')


@step("we fill all fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we fill all fields')


@when('we push "SUBMIT" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we push "SUBMIT" button')


@then('we see a "thanks" message')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then we see a "thanks" message')