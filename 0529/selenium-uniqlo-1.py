import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.uniqlo.com/tw/zh_TW/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(3)

# search = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[4]/div/ul/li[2]')
search = driver.find_element(By.CLASS_NAME, 'li-search')

search.click()

time.sleep(5)

driver.close()