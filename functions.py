from selenium import webdriver
from selenium.common import NoSuchElementException, JavascriptException
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def click_button(driver: webdriver):
    for i in range(5):
        try:
            driver.execute_script('document.getElementById("list_last").click()')
            time.sleep(1)
        except JavascriptException as e:
            break

def login(username, password, driver):
    driver.get("https://rivalregions.com")
    time.sleep(3)
    mail_field = driver.find_element("name", "mail")
    mail_field.send_keys(username)
    time.sleep(1)
    password_field = driver.find_element("name", "p")
    password_field.send_keys(password)
    time.sleep(1)
    password_field.submit()
    time.sleep(5)
    return driver