from selenium import webdriver
from selenium.common import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#pip install selenium
from auth import mail, password
from functions import click_button, login

# Set your mail and password variables here
chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver=login(mail, password, driver)
#Przejdź do parlamentu
driver.get("https://rivalregions.com/#parliament")
driver.refresh()
time.sleep(5)
# kliknij "New law"
driver.find_element(By.XPATH, '//*[@id="content"]/div[11]').click()
time.sleep(3)
#Rozwiń listę ustaw
driver.find_element(By.XPATH, '//*[@id="offer_dd"]/div/div').click()
time.sleep(2)
#Ustawa o odnowieniu złota
gold=driver.find_element(By.XPATH, '//*[@id="offer_dd"]/ul/li[5]/a')
#Dodatkowe sprawdzenie gdyby admin podmienił kolejność ustaw
if "Resources exploration" in gold.get_attribute('innerHTML'):
    gold.click()
    time.sleep(2)
    #Puść ustawę
    driver.find_element(By.XPATH, '//*[@id="offer_do"]').click()
else:
    print(gold.get_attribute('innerHTML'))