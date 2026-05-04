import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_employee_full_navigation_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://pai-erp-qa.pineappleai.cloud/login")

    try:
        # Login
        login_page = LoginPage(driver)
        login_page.login("PAI025", "Z!Dr5sLk$R")
        time.sleep(5)

        # Dashboard check
        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded()
        print("✅ Dashboard loaded")

        # Logout
        dashboard.logout()
        time.sleep(3)

        assert "login" in driver.current_url.lower()
        print("✅ Logout successful")

    finally:
        driver.quit()