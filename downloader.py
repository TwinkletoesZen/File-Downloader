from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()

browser.get("https://ca.finance.yahoo.com/quote/FM.TO/history?p=FM.TO")

def Download():
  try:
    File = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span'))
    )
    sleep(1)
    try:
      File.click()
    except:
      print("Download Failed")
          
  except:
    print("It didn't work")