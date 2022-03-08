from selenium.webdriver.common.by import By

class Header:

    HOME_BTN = (By.XPATH, "//h1[@class='site-title']")
    CART_ICON = (By.XPATH, "//div[@id='ast-desktop-header']//*[@class='count']")
    ACTIVE_OPTION = (By.XPATH, "//div[@id='ast-desktop-header']//a[@aria-current]")

    def __init__(self, driver):
        self._driver = driver

    def click_to_cart(self):
        self._driver.find_element(
            *self.CART_ICON).click()

    def click_to_home(self):
        self._driver.find_element(
            *self.HOME_BTN).click()

    def select_menu_option(self, option: str):
        """
        Click to selected option from menu \n
        
        Params: \n
        option - full case insensitive text of the menu option

        Usage: \n
        self.select_menu_option('Store')
        """
        self._driver.find_element(
            By.XPATH, f"//li/a[text()='{option.title()}']").click()

    @property
    def current_menu_option(self) -> str:
        """
        Returns name of a selected option in menu
        """
        return self._driver.find_element(
            *self.ACTIVE_OPTION).text

    @property
    def cart_items(self) -> int:
        """
        Returns number of items in the cart
        """
        return int(self._driver.find_element(
            *self.CART_ICON).text)