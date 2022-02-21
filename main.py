# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service('/Users/macbookpro/Desktop/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

menu = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab",
        "buyPortal", "buyTime machine"]

reversed_menu = [item for item in reversed(menu)]

five_minutes = time.time() + 60 * 1
five_seconds = time.time() + 5

while True:
    cookie.click()
    if time.time() > five_seconds:
        items = driver.find_elements(By.CSS_SELECTOR, '#store div')
        for item in items[::-1]:
            try:
                if not item.get_attribute('class'):
                    item.click()
            except StaleElementReferenceException:
                items = driver.find_elements(By.CSS_SELECTOR, '#store div')
        timeout = time.time() + 5

    if time.time() > five_minutes:
        cookies_per_second = driver.find_element(By.ID, 'cps')
        print(cookies_per_second.text)
        break

driver.quit()
