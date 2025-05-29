import time

import openpyxl
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.uniqlo.com/tw/zh_TW/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

time.sleep(3)

# search = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[4]/div/ul/li[2]')
search = driver.find_element(By.CLASS_NAME, 'li-search')

# search.click()
action.click(search).pause(5).perform()
# time.sleep(5)

ck = driver.find_element(By.ID, 'onetrust-accept-btn-handler')

# ck.click()
# time.sleep(3)
action.click(ck).pause(3).perform()

sale = driver.find_element(By.CSS_SELECTOR,'img[alt="特價商品"]')

# sale.click()
action.click(sale).perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'product-ul'))
)

time.sleep(2)

p_count = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    try:
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, 'loading-paging'))
        )
    except TimeoutException as e:
        print(e)
    products=driver.find_elements(By.CLASS_NAME, 'product-li')
    if p_count == len(products):
        break
    p_count = len(products)

products = driver.find_elements(By.CLASS_NAME, 'product-li')

# wb = openpyxl.Workbook()
# ws = wb.active
# ws.title = '女裝'

# ws.append(['商品名稱','代碼','價格','圖片連結'])

for product in products:
    title = product.find_element(By.CLASS_NAME, 'ec-font-sub-title').text
    price = product.find_element(By.CLASS_NAME, 'h-currency').text
    img = product.find_element(By.CLASS_NAME, 'picture-img')
    im = img.get_property('src')
    # print(f'{title}:{price}')
    # ws.append([title[:-6],title[-6:],price,im])
# wb.save('u.xlsx')
driver.close()