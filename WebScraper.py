from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

driver_path = 'D:/Projects/chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.collegecribs.ie/'
driver.get(url)
time.sleep(3)

SEARCH_INPUT_XPATH = '//div[contains(@class, "multiselect multiselect--place-left multiselect--no-arrow multiselect--auto is-searchable")]'

city = input("Enter The City You Want To Search: ")
search_input = driver.find_element(By.XPATH, SEARCH_INPUT_XPATH)
search_input.send_keys(city)
time.sleep(5)
search_input.send_keys(Keys.RETURN)
