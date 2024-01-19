import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture

def browser():
    driver = webdriver.Chrome(executable_path='C:\Users\DIVYA\Documents\selenium-bdd-cucumber-test\selenium-bdd-cucumber-test\Drivers)
    yield driver
    driver.quit()

def test_w3schools_logo_presence(browser):
    browser.get("https://www.w3schools.com/")
    try:
        logo_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, 'fa fa-logo ws-hover-text-green'))
        )
        assert logo_element.is_displayed(), "W3Schools logo is not displayed on the page."

    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

 