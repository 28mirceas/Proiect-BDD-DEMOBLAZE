from selenium.webdriver.common.by import By
from pages.base_page import BasePage



LOGIN_PAGE = "https://demoblaze.com"

class LoginPage(BasePage):

    # Login Page Locators
    BUTTON_LOGIN_MENU = (By.XPATH, "//a[@id='login2']")
    INPUT_USERNAME = (By.XPATH, "//input[@id='loginusername']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='loginpassword']")
    BUTTON_LOGIN = (By.XPATH, "//button[@onclick='logIn()']")
    BUTTON_MENU_NAME_USER = (By.XPATH, "//a[@id='nameofuser']")


    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LOGIN_PAGE)

    def click_login_menu(self):
        self.click(self.BUTTON_LOGIN_MENU)

    def set_username(self, user_text):
        self.type(self.INPUT_USERNAME, user_text)

    def set_password(self, pass_text):
        self.type(self.INPUT_PASSWORD, pass_text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def verify_user_menu_button(self, text):
        self.verify_text(self.BUTTON_MENU_NAME_USER, text)

    def get_error_alert_text(self):
        return self.get_alert_text()

    def accept_error_alert(self):
       self.accept_alert()

    def login(self, username, password):
        self.click_login_menu()
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

