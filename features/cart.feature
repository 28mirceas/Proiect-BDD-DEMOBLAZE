Feature: Verify the functionality of the cart page


  @cart
  @deleteProductFromCart
  Scenario: Delete a product from cart
    Given User adds product "Samsung galaxy s6" to cart
    And User adds product "Nexus 6" to cart
    And User adds product "Iphone 6 32gb" to cart
    When User opens the cart page
    And User deletes product "Samsung galaxy s6"
    Then Product "Samsung galaxy s6" is not displayed in the cart


  @cart
  @placeAnOrder
  Scenario: Place an order
    Given Product "Samsung galaxy s6" is added to cart
    When User opens the cart page
    And Click to button place order
    And Add "Sava Mircea" in purchase form name field
    And Add "RO" in purchase form country field
    And Add "Sector 5" in purchase form city field
    And Add "visa" in purchase form card field
    And Add "05" in purchase form month field
    And Add "29" in purchase form year field
    And Click to purchase button
    Then See the success purchase message "Thank you for your purchase!"