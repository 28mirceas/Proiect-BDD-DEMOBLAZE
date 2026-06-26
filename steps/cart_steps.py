from behave import given, when, then

@given('User adds product "{product_name}" to cart')
def step_impl(context, product_name):
    context.categories_page.click_product_link_title(product_name)
    context.categories_page.add_product_to_cart()
    context.categories_page.get_success_alert_text()
    context.categories_page.accept_success_alert()
    context.categories_page.click_link_home_page()


@given('Product "{product_name}" is added to cart')
def step_impl(context, product_name):
    context.categories_page.click_product_link_title(product_name)
    context.categories_page.add_product_to_cart()
    context.categories_page.get_success_alert_text()
    context.categories_page.accept_success_alert()


@when('User opens the cart page')
def step_impl(context):
    context.cart_page.open_cart()


@when('Click to button place order')
def step_impl(context):
    context.cart_page.click_place_order()


@when('Add "{purchase_name}" in purchase form name field')
def step_impl(context, purchase_name):
    context.cart_page.set_purchase_name(purchase_name)


@when('Add "{purchase_country}" in purchase form country field')
def step_impl(context, purchase_country):
    context.cart_page.set_purchase_county(purchase_country)


@when('Add "{purchase_city}" in purchase form city field')
def step_impl(context, purchase_city):
    context.cart_page.set_purchase_city(purchase_city)


@when('Add "{purchase_card}" in purchase form card field')
def step_impl(context, purchase_card):
    context.cart_page.set_purchase_card(purchase_card)


@when('Add "{purchase_month}" in purchase form month field')
def step_impl(context, purchase_month):
    context.cart_page.set_purchase_month(purchase_month)


@when('Add "{purchase_year}" in purchase form year field')
def step_impl(context, purchase_year):
    context.cart_page.set_purchase_year(purchase_year)


@when('Click to purchase button')
def step_impl(context):
    context.cart_page.click_button_purchase()


@when('User deletes product "{product_name}"')
def step_impl(context, product_name):
    context.cart_page.delete_product(product_name)


@then('Product "{product_name}" is not displayed in the cart')
def step_impl(context, product_name):
    context.cart_page.verify_product_not_in_cart(product_name)


@then('See the success purchase message "{expected_message}"')
def step_impl(context, expected_message):
    context.cart_page.verify_success_purchase_message(expected_message)