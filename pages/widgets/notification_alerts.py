from selenium.webdriver.common.by import By


class NotificationAlerts:

    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class,'alert-success')]")
    
    def __init__(self, driver):
        self._driver = driver