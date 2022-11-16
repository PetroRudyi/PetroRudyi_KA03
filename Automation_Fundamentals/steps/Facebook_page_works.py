from behave import *

use_step_matcher("re")


@when("we push Facebook icon")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we push Facebook icon')


@then('open "https://www\.facebook\.com/EPAM\.Global" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then open "https://www.facebook.com/EPAM.Global" page')


@given('we are at "https://www\.epam\.com/"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we are at "https://www.epam.com/"')