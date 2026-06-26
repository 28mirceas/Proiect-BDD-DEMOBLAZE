from behave import given, when, then

@given('Navigate to login page')
def steps_impl(context):
    context.login_page.open()

@when('Click to Log in button in the menu')
def steps_impl(context):
    context.login_page.click_login_menu()

@when('Enter "{user_text}" in the username input field')
def steps_impl(context, user_text):
    context.login_page.set_username(user_text)

@when('Enter "{pass_text}" in the password input field')
def steps_impl(context, pass_text):
    context.login_page.set_password(pass_text)

@when('Click Log in button')
def steps_impl(context):
    context.login_page.click_login_button()

@then('The new button added in the menu is "{button_text}"')
def steps_impl(context, button_text):
    context.login_page.verify_user_menu_button(button_text)

@then('See the login error "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.login_page.get_error_alert_text()
    assert actual_message == expected_message
    context.login_page.accept_error_alert()