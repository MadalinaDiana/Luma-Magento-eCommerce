Feature: HomePage

  Background:
    Given Opened HomePage website

  Scenario:  Search with empty field
    When Click on the 'search' input field.
    Then Search button is not displayed.

  Scenario: Search with valid input field
    When Click on the 'search' input field.
    And Enter in 'search' valid 'short' parameters.
    Then Search button is displayed.


  Scenario Outline: Click nav-bar buttons
    When Click the "<button>".
    Then The page with "<url>" is opened.
    Examples:
      | button     | url              |
      | What's New | what-is-new.html |
      | Women      | women.html       |
      | Men        | men.html         |
      | Gear       | gear.html        |
      | Training   | training.html    |
      | Sale       | sale.html        |

  Scenario Outline: Functionality of products
    When Scroll down on the page.
    And Click the "<measure>" measure.
    And Click on the "<color>".
    And Click on the "<action>" action.
    Examples:
      | measure | color  | action           |
      | option-label-size-143-item-166      | [aria-label="Blue"]   | (//button[@title='Add to Cart'])[1]      |
      | option-label-size-143-item-167       | [aria-label="Orange"] | (//a[@title='Add to Wish List'])[1]|
      | option-label-size-143-item-168       | [aria-label="Purple"] | (//a[@title='Add to Compare'])[1]  |
    Then Check the "My Cart" section.

    Scenario Outline: Send invalid/valid Email Subscription
      When Scroll down on the footer of the page.
      And Click on the 'newsletter' input field.
      And Enter in 'newsletter' valid '<email>' parameters.
      And Click on the "(//button[@title='Subscribe'])" action.
      Then Check the '<message>'.
       Examples:
      | email | message  |
      |  | This is a required field.  |
      | md | Please enter a valid email address (Ex: johndoe@domain.com).|
      | md@yahoo.com | |


