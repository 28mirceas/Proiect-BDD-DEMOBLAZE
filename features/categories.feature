Feature: Verify the functionality of the categories page

  @categories
  @viewProduct
  Scenario: Access the details page of the product
    Given Product "Samsung galaxy s6" details page is opened
    Then Verify the details page name is "Samsung galaxy s6"


  @categories
  @addProductToCart
  Scenario: Add a product to cart
   Given Add product "Samsung galaxy s6" to cart
    Then See the success message "Product added."