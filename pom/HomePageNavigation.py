import driver
from Base.SeleniumBase import SeleniumMethod
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomePageNavigation(SeleniumMethod):

    def __init__(self):
        super().__init__()
        self.driver = driver.wd

        self.navigation_links = '#sectionMenuModule li .ts-sidebar-item-text'
        self.navigation_links_in_page = 'Домашняя страница, Контрагенты, Контакты, Счета, Оплаты, Запросы, Проекты, Ставки подрядчиков, Платёжный календарь'


    def get_navigation_links(self) -> List[WebElement]:
        return self.are_visible('css', self.navigation_links, 'Header navigation links')

    def get_navigation_links_text(self) -> str:
        navigation_links = self.get_navigation_links()
        navigation_links_text = [link.text for link in navigation_links]
        return ', '.join(navigation_links_text)

    def payment_calendar(self):
        self.is_visible('id', 'sidebar-item-text-8').click()

