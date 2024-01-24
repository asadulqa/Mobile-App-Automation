from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BaseDriver:
    def __init__(self, driver=None,context=None):
        if context:
            self.driver = context.driver
        else:
            self.driver = driver

    def click(self, locator):
        self.wait_for_element_to_clickable(locator)
        self.driver.find_element(*self._formatter(locator)).click()

    def wait_for_element(self,locator,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self._formatter(locator)))

    def wait_for_element_to_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self._formatter(locator)))

    # def send_keys(self,id_xpath, locator):
    #     self.driver.find_element(id_xpath,locator)
    def _formatter(self,locator):
        type,loc = locator.split("@@")
        if type == "id":
            return (AppiumBy.ID,loc)
        if type =="xpath":
            return (AppiumBy.XPATH,loc)


