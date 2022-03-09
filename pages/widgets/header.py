from selenium.webdriver.common.by import By

class Header:

    LOGIN_OR_REGISTER = (By.ID, "login_link")

    def __init__(self, driver):
        self._driver = driver

    def click_to_login_or_register(self):
        self._driver.find_element(
            *self.LOGIN_OR_REGISTER).click()