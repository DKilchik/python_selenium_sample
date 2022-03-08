from utilities.webdriver.web import WebdriverExtension

class BasePage(WebdriverExtension):

    def __init__(self, driver):
        super().__init__(driver)