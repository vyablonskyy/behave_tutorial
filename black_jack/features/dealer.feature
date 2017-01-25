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

  # Tableized tests
  # Often when writing tests we want to test the same behavior against many different parameters and check the results
  # The next game logic to test is that the dealer knows the point value of its hand
  # Called a "Scenario Outline"
  # It uses parameters in angle brackets <hand>, <total> that correspond to the headers of the table
  # A table of inputs ("hand") and outputs ("total")
  Scenario Outline: Get hand total
    Given a <hand>
    When the dealer sums the cards
    Then the <total> is correct

    Examples: Hands
    | hand      | total |
    | 5, 7      | 12    |
    | 5, Q      | 15    |
    | Q, Q, A   | 21    |
    | Q, A      | 21    |
    | A, A, A   | 13    |