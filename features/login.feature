Feature: Test the login functionality

  Background: Open the login page
    Given Navigate to login page

  @login
  Scenario: Login as standard user with valid credentials
    When Click to Log in button in the menu
    And Enter "demoblaze" in the username input field
    And Enter "demoblaze" in the password input field
    And Click Log in button
    Then The new button added in the menu is "Welcome demoblaze"


  @negativeLogin
  Scenario: Login with wrong password
    When Click to Log in button in the menu
    And Enter "demoblaze" in the username input field
    And Enter "demoblaze1" in the password input field
    And Click Log in button
    Then See the login error "Wrong password."



