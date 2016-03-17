import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

countries = ['India', 'Germany', 'Singapore', 'South Africa']

for country in countries:
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)

    driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
        (By.ID, "countryName")))
        box.send_keys(country)
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.PARTIAL_LINK_TEXT, "Pay Monthly")))
        button.click()
        driver.find_element_by_xpath('//*[@id="paymonthly"]').click()
 
    except TimeoutException:
        print("Box or Button not found in google.com")
        continue

    time.sleep(2)
    element = driver.find_element_by_id("standardRatesTable")
    print element.text

driver.quit()
