from behave import *

use_step_matcher("re")


@given("we have driver initialized")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given we have driver initialized')


@when("we login successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we login successfully')


@step("we go to Pay Grades")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we go to Pay Grades')


@step("we add new Pay Grades")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we add new Pay Grades')


@then("we have new Pay Grades appeared")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then we have new Pay Grades appeared')


@step("we add new Currency")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we add new Currency')


@then("we have new Currency")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then we have new Currency')


@step("we remove Currency")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we remove Currency')


@step("we remove our Pay Grades")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And we remove our Pay Grades')