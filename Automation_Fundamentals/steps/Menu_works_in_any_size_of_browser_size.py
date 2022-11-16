from behave import *

use_step_matcher("re")


@given('we are at "https://www\.epam\.com" in any size of window')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we are at "https://www.epam.com" in any size of window')


@when("we (?P<menu>.+) button")
def step_impl(context, menu):
    """
    :type context: behave.runner.Context
    :type menu: str
    """
    raise NotImplementedError(u'STEP: When we <menu> button')


@then("(?P<do>.+) site show us menu points")
def step_impl(context, do):
    """
    :type context: behave.runner.Context
    :type do: str
    """
    raise NotImplementedError(u'STEP: Then <do> site show us menu points')