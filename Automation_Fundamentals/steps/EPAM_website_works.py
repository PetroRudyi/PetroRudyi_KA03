from behave import *

use_step_matcher("re")


@given("our web browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given our web browser')