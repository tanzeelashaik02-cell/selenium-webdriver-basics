"""
Basic Selenium WebDriver script demonstrating core browser-automation
fundamentals: locating elements, handling a dropdown, explicit waits and
assertions.

Target: the same public "XYZ Bank" demo sandbox used in the companion
Cypress project (https://www.globalsqa.com/angularJs-protractor/BankingProject),
Customer Login flow -> verifies the account dashboard loads for the
selected customer.

Kept intentionally simple (a single script, no page-object framework) to
demonstrate fundamental Selenium WebDriver concepts: locators, waits and
dropdown handling.

Run:
    pip install -r requirements.txt
    python test_customer_login_basic.py

Requires a local Chrome/Chromedriver installation compatible with the
installed Selenium version (Selenium 4 manages the driver automatically
via Selenium Manager).
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
CUSTOMER_NAME = "Harry Potter"  # one of the sample customers seeded on the demo


def test_customer_login_basic():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(BASE_URL)

        # 1. Go to the Customer Login screen
        customer_login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Customer Login']"))
        )
        customer_login_btn.click()

        # 2. Pick a customer from the dropdown (basic Select usage)
        dropdown = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select[ng-model='custId']"))
        )
        Select(dropdown).select_by_visible_text(CUSTOMER_NAME)

        # 3. Submit the login form
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # 4. Verify the account dashboard loaded with the expected content
        welcome_banner = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//strong[contains(text(),'{CUSTOMER_NAME}')]")
            )
        )
        assert welcome_banner.is_displayed(), "Expected the welcome banner to be visible after login"

        account_info = driver.find_element(By.XPATH, "//*[contains(text(),'Account Number')]")
        assert "Account Number" in account_info.text

        print("PASS: customer login basic flow verified successfully.")

    finally:
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    test_customer_login_basic()
