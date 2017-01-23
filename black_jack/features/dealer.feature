Feature: The dealer for the game of 21
  #Test when the round starts, the dealer should deal itself two cards
  # "Given" - initializes a state - our state is a new dealer object
  # "When" - describes an action - the round is starting
  # "Then" - states the expected outcome - the dealer has two cards
  Scenario: Deal initial cards
    Given a dealer
    When the round starts
    Then the dealer gives itself two cards
    # Think of a step as a task for Behave to execute
    # !!!The cycle is to write a test, see that it fails, and then write code to make the test pass