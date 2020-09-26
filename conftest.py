import pytest
from selenium import webdriver
from logzero import logger


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        dest='browser',
        default='chrome',
        choices=('chrome', 'firefox'),
        metavar='NAME',
        help='Browser name on which to run the UI tests.',
    )


@pytest.fixture(scope='session')
def browser(request):
    e = request.config.getoption('browser').lower()
    logger.debug(f'Browser: {e.lower()}')
    yield e


@pytest.fixture(scope='session')
def ui_driver(browser):
    capabilities = {
        'browserName': browser,
        'platform': 'ANY',
        'version': '',
        'acceptSslCerts': True
    }
    driver = webdriver.Remote(
        command_executor='http://selenium-host:4444/wd/hub',
        desired_capabilities=capabilities)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def api_base_url():
    return "https://reqres.in"
