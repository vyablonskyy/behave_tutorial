# The steps in Behave are the link between the descriptive tests in .feature files and actual application code

from behave import *
from twentyone import *


# Behave steps use annotation that match the names of the phases

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()


# It's important to notice that the text inside of the annotation matches the scenario text exactly.
# If it doesn't match, the test cannot run

# The context object is passed from step to step, and it is where we can store information to used by other steps.
# Since this step is a "given", we need to initialize our state.
# We do that by creating a Dealer object, and attaching that object to the context.


@when('the round starts')  # here we have access to the dealer created in "given"
def step_impl(context):
    context.dealer.new_round()  # and we can now call a method on that object


@then('the dealer gives itself two cards')  # we still have access to the dealer,
def step_impl(context):
    assert (len(context.dealer.hand) == 2)  # and we assert that the dealer has two cards in its hand
