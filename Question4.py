def initialize_browser():
    """Initialize and return a Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(executable_path=chromedriver_path, options=options)

def click_element(driver, by, value):
    """Click the element identified by the given 'by' and 'value'."""
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )
    element.click()

def enter_text(driver, by, value, text):
    """Enter text into the element identified by the given 'by' and 'value'."""
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, value))
    )
    element.clear()
    element.send_keys(text)

driver = initialize_browser()
url = "https://www.makemytrip.com/"
driver.get(url)

try:
    clickElement(driver, By.xpath("chNavIcon appendBottom2 chSprite chFlights active]"));
    clickElement(driver, By.xpath("/hsw_inputBox tripTypeWrapper"));

    enterText(driver, By.xpath("lbl_input latoBold font12 blueText appendBottom5"), "New Delhi");
    enterText(driver, By.xpath("lbl_input latoBold font12 blueText appendBottom5"), "Mumbai");

except Exception as e:
    print(f"An error occurred: {e}")
 
finally:
    driver.quit()

 