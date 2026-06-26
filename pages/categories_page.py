from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CategoriesPage(BasePage):
    # Categories Page Locators
    PRODUCT_PAGE_NAME = (By.XPATH, "//h2[text()='Samsung galaxy s6']")
    BUTTON_ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")
    BUTTON_HOME_MENU = (By.XPATH, "//a[text()='Home ']")


    def __init__(self, driver):
        super().__init__(driver)


    def click_product_link_title(self, product_name):
        product_link_locator = (By.XPATH, f"//a[text()='{product_name}']")
        self.click(product_link_locator)

    def verify_product_page_name(self, text):
        self.verify_text(self.PRODUCT_PAGE_NAME, text)

    def add_product_to_cart(self):
        self.click(self.BUTTON_ADD_TO_CART)

    def get_success_alert_text(self):
        return self.get_alert_text()

    def accept_success_alert(self):
        self.accept_alert()

    def click_link_home_page(self):
        self.click(self.BUTTON_HOME_MENU)
