from .base_page import BasePage
from configuration import config


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.HOST