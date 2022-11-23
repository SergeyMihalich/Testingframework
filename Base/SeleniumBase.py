
import driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from typing import List




class SeleniumMethod():
    def __init__(self):
        self.driver = driver.wd
        self.wait = WebDriverWait(self.driver, 20)

    def __get_selenium_method(self, fiend_by: str) -> dict:
        fiend_by = fiend_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'tag_name': By.TAG_NAME,
        }
        return locating[fiend_by]

    def is_visible(self, fiend_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_method(fiend_by), locator)), locator_name)

    def to_be_clickable(self, fiend_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable((self.__get_selenium_method(fiend_by), locator)), locator_name)

    def is_presence(self, fiend_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.__get_selenium_method(fiend_by), locator)), locator_name)

    def invisibility(self, fiend_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.__get_selenium_method(fiend_by), locator)), locator_name)

    def are_visible(self, fiend_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_method(fiend_by), locator)), locator_name)

    def are_presence(self, fiend_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located((self.__get_selenium_method(fiend_by), locator)), locator_name)
