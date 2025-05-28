import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://google.com')

driver.maximize_window()

driver.save_screenshot('google.png')

time.sleep(2)

driver.get('https://tw.yahoo.com')

driver.save_screenshot('yahoo.png')

time.sleep(2)

driver.close()