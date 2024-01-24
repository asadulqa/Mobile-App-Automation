import pytest
from appium import webdriver


@pytest.fixture()
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'itel S23',
        'appPackage': 'com.splendapps.splendo',
        'appActivity': 'com.splendapps.splendo.MainActivity',
        'automationName': 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()
