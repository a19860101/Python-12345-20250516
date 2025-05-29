import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.uniqlo.com/tw/zh_TW/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(3)

# search = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[4]/div/ul/li[2]')
search = driver.find_element(By.CLASS_NAME, 'li-search')

search.click()

time.sleep(5)

ck = driver.find_element(By.ID, 'onetrust-accept-btn-handler')

ck.click()

time.sleep(3)

sale = driver.find_element(By.CSS_SELECTOR,'img[alt="特價商品"]')

sale.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'product-ul'))
)

time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, 'product-li')

for product in products:
    title = product.find_element(By.CLASS_NAME, 'ec-font-sub-title').text
    price = product.find_element(By.CLASS_NAME, 'h-currency').text
    print(f'{title}:{price}')

driver.close()