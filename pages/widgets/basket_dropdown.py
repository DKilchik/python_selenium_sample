from selenium.webdriver.common.by import By


class BasketDropDown:

    DROPDOWN = (By.XPATH, "//button[@data-toggle='dropdown']")
    TOTAL = (By.XPATH, "//p[@class='text-right']/small")
    QTY_COLUMN = (By.XPATH, "//div[contains(@class,'text-center')]")


    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.find_element(
            *self.DROPDOWN).click()

    @property
    def total_price(self) -> float:
        text = self._driver.find_element(*self.TOTAL).text
        for word in text.split():
            for symbol in word:
                if symbol.isdigit():
                    return float(word.replace("£", ""))
        return None

    @property
    def items_number(self) -> int:
        rows = self._driver.find_elements(*self.QTY_COLUMN)
        if len(rows) == 0:
            return 0
        return sum([int(row.text.split()[1]) for row in rows])
