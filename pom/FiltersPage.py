from asyncio import sleep

from selenium.webdriver import ActionChains, Keys

import driver
from Base.SeleniumBase import SeleniumMethod


class FilterPage(SeleniumMethod):
    def __init__(self):
        super().__init__()
        self.driver = driver.wd

    def check_filter(self):
        self.is_visible('css', '#customFilterButtonContainer_SectionModuleV2_McsPaymentSchedule1052af83Section_QuickFilterModuleV2 .t-btn-text.t-btn-left')
        if self.invisibility('ID', "t-comp166-textEl"):
            web_elements = self.are_visible('CLASS_NAME',
                                            "t-btn-wrapper.t-btn-no-text-padding.t-btn-style-transparent.filter-remove-button")
            try:
                for web_element in web_elements:
                    click_id = web_element.get_attribute("id")
                    self.is_visible('ID', click_id).click()
            except:
                pass

        self.to_be_clickable('CLASS_NAME', "filter-inner-container.custom-filter-button-container").click()
        self.to_be_clickable('css', "[data-item-marker='Добавить условие'").click()

        tab_filter_1 = self.is_visible('css', ".base-edit.ts-box-sizing.base-edit-with-right-icon.filter-simple-filter-edit")
        ActionChains(self.driver).move_to_element(tab_filter_1).click(tab_filter_1).perform()
        self.to_be_clickable('css', "li[data-item-marker='Валюта'").click()

        tab_filter_2 = self.is_visible('ID', "customFilterSectionModuleV2_McsPaymentSchedule1052af83Section_QuickFilterModuleV2-el")
        ActionChains(self.driver).move_to_element(tab_filter_2).click(tab_filter_2).send_keys("Рубль", Keys.ENTER).perform()
        sleep(5)