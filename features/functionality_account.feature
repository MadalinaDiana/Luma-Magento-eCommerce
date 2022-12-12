Feature: Account functionality

  Background:
    Given Opened the Sign in page.
    When Enter in 'email' valid 'ab@yahoo.com' parameters.
    And Enter in 'pass' valid 'abc123!))' parameters.
    And Click the "send2" measure.
    Then The page redirect to the "customer/account/" page.

 @scenario_setup
  Scenario: Buy items
    When Click the "Sale".
    And Click the "Jackets".
    And Click the "option-label-size-143-item-167" measure.
    And Click the "option-label-color-93-item-50" measure.
    And Click on the "(//button[@title='Add to Cart'])[1]" action.
    And Scroll up on the page.
    When Click on the "/html/body/div[2]/header/div[2]/div[1]/a" action.
    And Click the "top-cart-btn-checkout" from my cart.
    Then The page redirect to the "checkout/#shipping" page.
    And Click "//*[@id="shipping-method-buttons-container"]/div/button" submit.
    And Click "//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button" submit.
    Then Check the 'Thank you for your purchase!'.
 @scenario_setup
  Scenario: Write review
    When Click the "My Wish List".
    And Click on the "(//*[@class="product-item-photo"])[1]" action.
    And Click on the 'tab-label-reviews-title' input field.
    And Click the "Rating_2_label" measure.
    And Enter in 'summary_field' valid 'Not a great shirt' parameters.
    And Enter in 'review_field' valid 'could be a better product, but it is not.' parameters.
    And Click on the "//*[@id="review-form"]/div/div/button" action.
    Then Check the 'You submitted your review for moderation.'.
 @scenario_setup
  Scenario Outline: Compare products
    When Click the "<button>".
    And Click the "<option>".
    And Click the "<measure>" measure.
    And Click on the "<color>".
    And Click on the "<action>" action.
    Examples:
      | button | option  | measure                        | color               | action                            |
      | Women  | Jackets | option-label-size-143-item-167 | [aria-label="Blue"] | (//a[@title='Add to Compare'])[1] |
      | Men    | Jackets | option-label-size-143-item-167 | [aria-label="Blue"] | (//a[@title='Add to Compare'])[1] |
    And Click the "comparison list".
    And Click on the "//tbody/tr/td[1]/div[2]/div[2]/a[1]" action.
    Then The page redirect to the "wishlist/index/index/wishlist_id/20668/" page.
 @scenario_setup
  Scenario: Update My Wish List
    When Click the "My Wish List".
    And Hover on the "(//*[@class="product-item-photo"])[1]" button.
    And Click on the "(//*[@title="Remove Item"])[1]" action.
    Then The message contain "has been removed from your Wish List.".