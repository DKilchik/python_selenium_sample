from selenium.webdriver.common.by import By
from .base_page import BasePage
from configuration import config


class CataloguePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.HOST

    def add_item_to_basket(self, item_number=1):
        self._driver.find_element(
            By.XPATH, f"(//button[text()='Add to basket'])[{item_number}]").click()