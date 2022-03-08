import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()