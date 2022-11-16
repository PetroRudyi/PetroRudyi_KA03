from behave import *

use_step_matcher("re")


@given('we are at "https://www\.epam\.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we are at "https://www.epam.com"')


@when('we push "Contact us" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we push "Contact us" button')


@then('open "https://www\.epam\.com/about/who-we-are/contact" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then open "https://www.epam.com/about/who-we-are/contact" page')


@when('we press icon "EPAM" in the upper left corner')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we press icon "EPAM" in the upper left corner')


@then("website show us main page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then website show us main page')