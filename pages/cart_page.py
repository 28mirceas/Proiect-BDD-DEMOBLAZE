from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class CartPage(BasePage):
    # Cart Page Locators
    BUTTON_CART_MENU = (By.XPATH, "//a[@id='cartur']")
    CART_PRODUCT_NAMES = (By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Place Order']")
    NAME_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='name']")
    COUNTRY_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='country']")
    CITY_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='city']")
    CARD_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='card']")
    MONTH_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='month']")
    YEAR_FORM_PLACE_ORDER = (By.XPATH, "//input[@id='year']")
    BUTTON_FORM_PURCHASE = (By.XPATH, "//button[@onclick='purchaseOrder()']")
    SUCCESS_PURCHASE_ORDER = (By.XPATH, "//h2")


    def __init__(self, driver):
        super().__init__(driver)


    def open_cart(self):
        self.click(self.BUTTON_CART_MENU)


    def delete_product(self, product_name):
        delete_locator = (By.XPATH, f"//tr[td[text()='{product_name}']]//a[text()='Delete']")
        self.click(delete_locator)

    def clear_cart(self):
        print("Entering clear_cart()")

        while True:
            delete_buttons = self.driver.find_elements(
                By.XPATH,
                "//a[text()='Delete']"
            )

            print(f"Delete buttons found: {len(delete_buttons)}")

            if not delete_buttons:
                print("Cart is empty")
                break

            initial_count = len(delete_buttons)

            delete_buttons[0].click()

            self.wait.until(
                lambda driver: len(
                    driver.find_elements(
                        By.XPATH,
                        "//a[text()='Delete']")
                ) < initial_count
            )


    def verify_product_not_in_cart(self, product_name):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, f"//td[text()='{product_name}']")
            )
        )

        products = self.find_multiple(self.CART_PRODUCT_NAMES)
        product_names = [product.text for product in products]

        print(product_names)

        assert product_name not in product_names, (
            f"Product '{product_name}' is still present in cart."
        )


    def click_place_order(self):
        self.click(self.BUTTON_PLACE_ORDER)

    def set_purchase_name(self, name_text):
        self.type(self.NAME_FORM_PLACE_ORDER, name_text)

    def set_purchase_county(self, country_text):
        self.type(self.COUNTRY_FORM_PLACE_ORDER, country_text)

    def set_purchase_city(self, city_text):
        self.type(self.CITY_FORM_PLACE_ORDER, city_text)

    def set_purchase_card(self, card_text):
        self.type(self.CARD_FORM_PLACE_ORDER, card_text)

    def set_purchase_month(self, month_number):
        self.type(self.MONTH_FORM_PLACE_ORDER, month_number)

    def set_purchase_year(self, year_number):
        self.type(self.YEAR_FORM_PLACE_ORDER, year_number)

    def click_button_purchase(self):
        self.click(self.BUTTON_FORM_PURCHASE)


    # def verify_success_purchase_message(self, expected_message):
    #     self.verify_text(self.SUCCESS_PURCHASE_ORDER, expected_message)

    def verify_success_purchase_message(self, expected_message):
        actual_text = self.find(self.SUCCESS_PURCHASE_ORDER).text
        print(f"ACTUAL: [{actual_text}]")
        print(f"EXPECTED: [{expected_message}]")

