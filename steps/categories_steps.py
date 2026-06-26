from behave import given, when

@given('Add product "{product_name}" to cart')
def step_impl(context, product_name):
    context.categories_page.click_product_link_title(product_name)
    context.categories_page.add_product_to_cart()


@given('Product "{product_name}" details page is opened')
def step_impl(context, product_name):
    context.categories_page.click_product_link_title(product_name)


@then('Verify the details page name is "{expected_product_name}"')
def step_impl(context, expected_product_name):
    context.categories_page.verify_product_page_name(expected_product_name)


@then('See the success message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.categories_page.get_success_alert_text()
    assert actual_message == expected_message
    context.categories_page.accept_success_alert()
