# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.driver.implicitly_wait(timeout)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def open(self, url):
        self.driver.get(url)
