import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Parameter to run in headless mode
    parser.addoption('--headless', action='store', default=False,
                     help='To run in headless mode add to cmd "--headless=True"')



@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    headless_mode = request.config.getoption("headless")
    if headless_mode:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
    driver = Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()