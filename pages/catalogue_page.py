from selenium.webdriver.common.by import By
from .base_page import BasePage
from configuration import config
from utilities.allure import step



class CataloguePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.HOST

    @step
    def add_item_to_basket(self):
        self._driver.find_element(
            By.XPATH, "//button[text()='Add to basket']").click()
