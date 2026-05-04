from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    EMPLOYEE_ID = (By.XPATH, "//input[@placeholder='Enter your username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login')]")

    def login(self, username, password):
        self.type(self.EMPLOYEE_ID, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
