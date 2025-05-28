import os
import urllib.request as req

import openpyxl
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://www.uniqlo.com/tw/zh_TW/c/feature-sale-men.html'

action = ActionChains(driver)

driver.get(url)
# time.sleep(10)
p_c = 0

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,'product-li'))
)

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    products = driver.find_elements(By.CLASS_NAME, 'product-li')
    if p_c == len(products):
        break
    p_c = len(products)
    time.sleep(5)
    # try:
    #     WebDriverWait(driver, 10).until_not(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'loading-paging'))
    #     )
    # except Exception as e:
    #     print(e)


products = driver.find_elements(By.CLASS_NAME, 'product-li')
# ec-font-sub-title, h-currency

wb = openpyxl.Workbook()
ws = wb.active
for p in products:
    title = p.find_element(By.CLASS_NAME, 'ec-font-sub-title').text
    price = p.find_element(By.CLASS_NAME, 'h-currency').text
    img = p.find_element(By.CLASS_NAME, 'picture-img')
    os.makedirs('uq', exist_ok=True)
    # print(f'{title}:{price}')
    ws.append([title,title[-6:], price])
wb.save('uq.xlsx')







