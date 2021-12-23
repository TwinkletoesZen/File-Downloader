from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://query1.finance.yahoo.com/v7/finance/download/FM.TO?period1=1608692260&period2=1640228260&interval=1d&events=history&includeAdjustedClose=true")


