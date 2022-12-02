from features.pages.base_page import BasePage
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class CreateAccount(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"

    def enter_values(self, firstname, lastname, email, password, confpassword):
        self.driver.find_element(By.ID, 'firstname').send_keys(firstname)
        self.driver.find_element(By.ID, 'lastname').send_keys(lastname)
        self.driver.find_element(By.ID, 'email_address').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'password-confirmation').send_keys(confpassword)

    def click_submit(self):
        self.driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()