from selenium.webdriver.common.by import By
from .basket_dropdown import BasketDropDown

class Header:

    LOGIN_OR_REGISTER = (By.ID, "login_link")
    VIEW_BASKET = (By.XPATH, "//button[@onclick]")
    BASKET_BLOCK = (By.XPATH, "//div[contains(@class,'basket-mini')]")

    def __init__(self, driver):
        self._driver = driver
        self.basket_dropdown = BasketDropDown(self._driver)

    def click_to_login_or_register(self):
        self._driver.find_element(
            *self.LOGIN_OR_REGISTER).click()

    def click_to_view_basket(self):
        self._driver.find_element(
            *self.VIEW_BASKET).click()

    @property
    def total_cost(self) -> float:
        block_text = self._driver.find_element(*self.BASKET_BLOCK).text
        for word in block_text.split():
            for symbol in word:
                if symbol.isdigit():
                    return float(word.replace("£","").replace(",","."))
        return None

