Feature: Verify Sign In

  Background:
    Given Opened the Sign in page.

    Scenario Outline: Verify the buttons
      When Click the "<button>".
      Then The page redirect to the "<url>" page.
      Examples:
        | button                | url                              |
        | Forgot Your Password? | customer/account/forgotpassword/ |
        | Create an Account     | customer/account/create/         |
    Scenario: Sign in account

      When Enter in 'email' valid 'ab@yahoo.com' parameters.
      And Enter in 'pass' valid 'abc123!))' parameters.
      And Click the "send2" measure.
      Then The page redirect to the "customer/account/" page.





