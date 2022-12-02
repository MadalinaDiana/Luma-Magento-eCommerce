from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


class HomePage(BasePage):
    URL = "https://magento.softwaretestingboard.com/"

    def click_input_search_field(self, field):
        self.driver.find_element(By.ID, field).click()

    def input_data(self, field, value):
        self.driver.find_element(By.ID, field).send_keys(value)

    def button_status(self):
        button = self.driver.find_element(By.XPATH, '//*[@title="Search"]')
        try:
            button.click()
            status = True
        except ElementClickInterceptedException as e:
            status = False
        return status

    def go_to(self, button):
        element = self.driver.find_element(By.LINK_TEXT, button)
        element.click()

    def measure_selector(self, measure):
        element = self.driver.find_element(By.XPATH, f'//*[@id="{measure}"]')
        element.click()

    def color_selector(self, color):
        element = self.driver.find_element(By.CSS_SELECTOR, f'{color}')
        element.click()

    def action_selector(self, action):
        element = self.driver.find_element(By.XPATH, f'{action}')
        element.click()

    def check_message(self, message):
        if len(message) == 0:
            text = ''
        else:
            message = self.driver.find_element(By.XPATH, f"//*[contains(text(),'{message}')]")
            text = message.text
        return text
