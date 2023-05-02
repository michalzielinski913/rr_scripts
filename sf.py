from selenium import webdriver
from selenium.common import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#pip install selenium
from auth import mail, password
from functions import click_button, login

wars=["https://rivalregions.com/#war/details/519882",
      "https://rivalregions.com/#war/details/519888",
      "https://rivalregions.com/#war/details/519889",
      "https://rivalregions.com/#war/details/519964",
      "https://rivalregions.com/#war/details/520576",
      "https://rivalregions.com/#war/details/520867"]

players=[124479462510837, 2000935340, 1972096530540726]
wars=list(set(wars))
players=list(set(players))
# Set your mail and password variables here
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver=login(mail, password, driver)

sum=0
for player in players:
    driver.get("https://rivalregions.com/#war/in/{}".format(player))
    driver.refresh()
    time.sleep(5)
    click_button(driver)
    for war in wars:
        id = war.split("/")[-1]
        try:
            row=driver.find_element(By.CSS_SELECTOR, "[user='{}']".format(id))
            val = row.find_element("xpath","td[5]").text.replace(".", "").split(" ")[0]
            sum+=int(val)
            print("Player {} dealt {} in war {}".format(player,val,id))
        except NoSuchElementException:
            print("No participation in war {} for player".format(id, player))
print("Total: {}".format(sum))
