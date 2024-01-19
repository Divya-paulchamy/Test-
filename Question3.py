from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver_path = 'C:\Users\DIVYA\Documents\selenium-bdd-cucumber-test\selenium-bdd-cucumber-test\Drivers'
driver = webdriver.Firefox(executable_path=geckodriver_path)

url = "https://www.makemytrip.com/"
driver.get(url)

try:
    logo_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//imgak.mmtcdn.com/pwa_v3/pwa_hotel_assets/header/logo@2x.png'))
    )
    if logo_element.is_displayed():
        print("MakeMyTrip logo is present on the page.")
    else:
        print("MakeMyTrip logo is not displayed on the page.")
 
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()