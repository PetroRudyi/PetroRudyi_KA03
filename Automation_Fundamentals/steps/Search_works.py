from behave import *

use_step_matcher("re")


@given('go to "https://www\.epam\.com/search"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given go to "https://www.epam.com/search"')