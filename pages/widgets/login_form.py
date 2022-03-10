from selenium.webdriver.common.by import By
from configuration import config

class LoginForm:

    EMAIL_FLD = (By.NAME, "login-username")
    PASSWORD_FLD = (By.NAME, "login-password")
    LOG_IN_BTN = (By.NAME, "login_submit")

    def __init__(self, driver):
        self._driver = driver

    def send_email(self, email: str):
        email_fld = self._driver.find_element(
            *self.EMAIL_FLD)
        email_fld.send_keys(email)

    def send_password(self, password: str):
        password_fld = self._driver.find_element(
            *self.PASSWORD_FLD)
        password_fld.send_keys(password)

    def click_to_login_btn(self):
        self._driver.find_element(
            *self.LOG_IN_BTN).click()

    def login(self, email=config.USERNAME, password=config.PASSWORD):
        self.send_email(email)
        self.send_password(password)
        self.click_to_login_btn()
    