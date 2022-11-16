from behave import *

use_step_matcher("re")


@given("go to any non-existent page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given go to any non-existent page')