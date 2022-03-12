import pytest
import allure
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Parameter to run in headless mode
    parser.addoption("--headless", action="store", default=False,
                     help="To run in headless mode add to cmd '--headless=True'")
    # Parameter to set user language
    parser.addoption("--lang", action="store", default="en-gb", 
                     help="Set webdriver language")



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    This function helps: 
    to detect that some test failed and pass this information to teardown
    """
    outcome = yield 
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)



@pytest.fixture
def driver(request):
    chrome_options = Options()
    user_language = request.config.getoption("lang")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    headless_mode = request.config.getoption("headless")
    if headless_mode:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
    driver = Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture
def log_on_failure(request, driver):
    """
    Generate and attach screenshot to allure report  
    for failed test
    """
    yield
    if request.node.rep_call.failed:
        try:
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            # TODO remove it, when logger will be added
            print(e)