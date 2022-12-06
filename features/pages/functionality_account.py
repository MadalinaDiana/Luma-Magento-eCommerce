from features.pages.base_page import BasePage
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AccountFunction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.URL = "https://magento.softwaretestingboard.com/customer/account/"

    def check_contain(self, message):
        element = self.driver.find_element(By.XPATH, f'//div[contains(text(),"{message}")]')
        if element:
            status = True
        else:
            status = False
        return status

    def hover_button(self, value):
        select_elem = self.driver.find_element(By.XPATH, f'{value}')
        self.action.move_to_element(select_elem).perform()
