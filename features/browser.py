from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_current_url(self):
        return self.driver.current_url

    def click_item_id(self, value):
        element = self.driver.find_element(By.ID, f'{value}')
        element.click()

    def click_item_xpath(self, value):
        element = self.driver.find_element(By.XPATH, f'{value}')
        element.click()

    def close(self):
        self.driver.quit()

    def scroll_down(self, to):
        self.driver.execute_script(f"window.scrollTo(0, {to})")

    def scroll_up(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)