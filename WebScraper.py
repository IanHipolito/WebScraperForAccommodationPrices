from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

driver_path = 'D:/Projects/chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.collegecribs.ie/'
driver.get(url)
time.sleep(300)