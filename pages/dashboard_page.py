from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):

    DASHBOARD_MENU = (By.XPATH, "//span[contains(text(),'Dashboard')]")
    LOGOUT_MENU = (By.XPATH, "//a[.//span[contains(text(),'Logout')]]")

    def is_dashboard_loaded(self):
        return self.is_visible(self.DASHBOARD_MENU)

    def logout(self):
        self.click(self.LOGOUT_MENU)
        