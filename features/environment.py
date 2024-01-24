# from selenium import webdriver
from appium import webdriver
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': 'itel S23',
    'appPackage': 'com.splendapps.splendo',
    'appActivity': 'com.splendapps.splendo.MainActivity',
    'automationName': 'UiAutomator2'
}

def before_scenario(context, scenario):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(3)

def after_scenario(context, scenario):
    context.driver.quit()
