import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        capabilities = {
            "browserName": 'chrome',


            "browserVersion": '104.0',
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
    elif browser_name == "firefox":
        capabilities = {
            "browserName": 'firefox',
            "browserVersion": '104.0',
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
    else:
        raise pytest.UsageError('--browser_name should be "chrome" or "firefox"')
    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    yield browser
    browser.quit()
