from utilities.webdriver.web import WebdriverExtension
from .widgets import Header, NotificationAlerts

class BasePage(WebdriverExtension):

    # TODO adding complete description
    """
    This layer is used to interact to the business logic of an product.
    All webdriver wrappers are taken out to parent layer (WebdriverExtension class) 
    and can be reused at any projects.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self._driver)
        self.notification_alerts = NotificationAlerts(self._driver)