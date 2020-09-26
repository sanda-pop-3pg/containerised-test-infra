import time
from logzero import logger


def test_reqres(ui_driver):
    ui_driver.get('https://reqres.in/')
    logger.info(f"Reqres page title is: {ui_driver.title}")
    time.sleep(2)


def test_redhat(ui_driver):
    ui_driver.get('http://redhat.com')
    logger.info(f"RedHat page title is: {ui_driver.title}")
    time.sleep(2)
