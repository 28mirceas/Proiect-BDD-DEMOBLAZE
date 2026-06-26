from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_multiple(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def select_item_by_text(self, locator, text):
        dropdown_element = self.wait.until(EC.element_to_be_clickable(locator))
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(text)

    def verify_current_url(self, expected_url):
        assert self.driver.current_url == expected_url, \
            (f"Ëxpected URL: {expected_url}, " f"but got: {self.driver.current_url}")

    def verify_text(self, locator, expected_text):
        self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))
        actual_text = self.find(locator).text

        assert actual_text == expected_text, (
            f"Expected text:'{expected_text}', "
            f"but got:'{actual_text}'"
        )


    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text


    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()



