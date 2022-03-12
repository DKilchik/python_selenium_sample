from selenium.webdriver.common.by import By


class NotificationAlerts:

    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class,'alert-success')]")
    DEFERRED_BENEFIR_OFFER_ALERT = (
        By.XPATH, "//div[@class='alertinner ']/strong[text()='Deferred benefit offer']")
    
    def __init__(self, driver):
        self._driver = driver