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
wars=list(set(wars))
party_to_check="323630"
# Set your mail and password variables here

chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

driver=login(mail, password, driver)
sum=0
for war in wars:
    id=war.split("/")[-1]
    driver.get("https://rivalregions.com/#listed/partydamage/{}".format(id))
    driver.refresh()
    time.sleep(5)
    click_button(driver)
    try:
        row=driver.find_element(By.CSS_SELECTOR, "[user='{}']".format(party_to_check))
        val = row.find_element("xpath","td[3]").text.replace(".", "")
        sum+=int(val)
        print("You dealt {} dmg in war {}".format(val,id))
    except NoSuchElementException:
        print("No participation in war {}".format(id))
print("Total: {}".format(sum))
