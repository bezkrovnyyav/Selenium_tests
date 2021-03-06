from selenium.webdriver import Ie, Firefox, Chrome
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions

import pytest


def pytest_addoption(parser):
    # Register a command line option
    parser.addoption("--browser",
                     action="store",
                     default="Firefox",
                     help="web driver type")
    parser.addoption("--url",
                     action="store",
                     default="https://demo.opencart.com/",
                     help="base url")
    parser.addoption("--driver_path",
                     action="store",
                     default="drivers/",
                     help="relative path to the browser driver")


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def demo_url():
    return "https://www.demo-opencart.com/"


@pytest.fixture(scope="module")
def driver_path(request):
    return request.config.getoption("--driver_path")


@pytest.fixture(scope="module")
def browser(request, driver_path):

    # setup
    name = request.config.getoption("--browser")
    if name == "Chrome":
        options = ChromeOptions()
        options.add_argument("headless")
        options.add_argument("start-maximized")
        wd = Chrome(executable_path=driver_path+"chromedriver", options=options)
    elif name == "Firefox":
        options = FirefoxOptions()
        options.add_argument("headless")
        options.add_argument("start-maximized")
        wd = Firefox(executable_path=driver_path+"geckodriver", options=options)
    elif name == "Ie":
        options = IeOptions()
        options.add_argument("headless")
        options.add_argument("start-maximized")
        wd = Ie(options=options)
    else:
        print(f"Неизвестный тип браузера \"{name}\"")
        return None

    yield wd

    # teardown
    wd.quit()






