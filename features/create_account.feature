Feature: Create account

  Scenario Outline: Invalid/Valid input data
    Given  Opened the Create account page.
    When Enter invalid/valid "<firstname>","<lastname>","<email>","<password>" and "<confpassword>" input.
    And Click submit button.
    Then Check the '<message>'.

    Examples:
      | firstname | lastname | email | password  | confpassword | message                                                                                                               |
      | Luna      | Maria    | ab            | abc123!)) | abc123!))             | Please enter a valid email address (Ex: johndoe@domain.com).                                                        |
      | Women     | Lc       | abc@yahoo.com | 123       | 123                   | Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.  |
      | cb        | cc       | ab@yahoo.com  | abc123!)) | 123                   | Please enter the same value again.                                                                                  |
      | cb        | cc       | ab@yahoo.com  | abc123!)) | abc123!))             |                                                                                                                     |