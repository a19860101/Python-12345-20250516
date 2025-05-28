import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://google.com')
time.sleep(3)
driver.maximize_window()
time.sleep(2)

search = driver.find_element(By.CLASS_NAME, 'gLFyf')
# search.send_keys('Python', Keys.ENTER)
search.send_keys('P')
time.sleep(1)
search.send_keys('y')
time.sleep(2)
search.send_keys('t')
time.sleep(1)
search.send_keys('h')
time.sleep(3)

search.send_keys('o')
time.sleep(2)
search.send_keys('n')
time.sleep(5)

search.send_keys(Keys.ENTER)

time.sleep(15)


driver.close()