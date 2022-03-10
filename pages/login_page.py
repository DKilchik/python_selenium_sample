from .base_page import BasePage
from configuration import config
from .widgets import LoginForm

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.HOST + "accounts/login/"
        self.login_form = LoginForm(self._driver)
