import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://google.com')

driver.maximize_window()

search = driver.find_element(By.CLASS_NAME, 'gLFyf')
search.send_keys('Python')

time.sleep(5)


driver.close()