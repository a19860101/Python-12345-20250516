import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/w/mens-accessories-equipment-awwpwznik1'

driver.get(url)
driver.maximize_window()


p_count = 0
# for i in range(2):
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1500)')
    # time.sleep(2)
    # loader-bar
    try:
        # WebDriverWait(driver, 10).until_not(
        #     EC.presence_of_element_located((By.CLASS_NAME, 'loader-bar'))
        # )
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bar'))
        )
    except Exception as e:
        print(e)
    products = driver.find_elements(By.CLASS_NAME, 'product-card__info')
    print(len(products))
    if p_count == len(products):
        break
    p_count = len(products)

infos = driver.find_elements(By.CLASS_NAME, 'product-card__info')

print(len(infos))

# wb = openpyxl.Workbook()
# ws = wb.active

# ws.append(['商品名稱','商品分類','價格'])

for info in infos:
    # print(info.text)
    title = info.find_element(By.CLASS_NAME, 'product-card__title').text
    subtitle = info.find_element(By.CLASS_NAME, 'product-card__subtitle').text
    price = info.find_element(By.CLASS_NAME, 'product-card__price').text

    if '折扣' in price:
        print(f'{title}:{subtitle}:{price}')
        # ws.append([title, subtitle, price])

# wb.save('nike.xlsx')
driver.close()