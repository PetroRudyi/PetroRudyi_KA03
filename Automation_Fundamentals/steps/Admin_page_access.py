from behave import *

use_step_matcher("re")


@given("we are not admin")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we are not admin')


@when('we go to "https://www\.epam\.com/root"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we go to "https://www.epam.com/root"')


@then("website show us 404 page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then website show us 404 page')


@when('we print our request in field and press "FIND"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we print our request in field and press "FIND"')


@then("page update and show result for our request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then page update and show result for our request')


@when('we input "https://www\.epam\.com" into the browser')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we input "https://www.epam.com" into the browser')


@then("EPAM website load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then EPAM website load')