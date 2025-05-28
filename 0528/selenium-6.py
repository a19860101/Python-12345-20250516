import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/'

driver.get(url)
driver.maximize_window()

# 用xpath抓
# link1 = driver.find_element(By.XPATH, '//*[@id="gen-nav-commerce-header-v2"]/nav/header/div/div/div[2]/nav/ul/li[2]/div/a')
# 用link_text抓
link1 = driver.find_element(By.LINK_TEXT, '男款')
link1.click()
time.sleep(3)

# link2 = driver.find_element(By.XPATH, '//*[@id="eb498498-e1e0-4ad6-b689-ab3374ff3bca"]/div/div/nav/div[1]/ul/li[1]/a')
link2 = driver.find_element(By.LINK_TEXT, '運動裝備')
link2.click()
time.sleep(2)

# for i in range(5):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1500)')
#     time.sleep(2)

p_count = 0
# for i in range(2):
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1500)')
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'product-card__info')
    print(len(products))
    if p_count == len(products):
        break
    p_count = len(products)

infos = driver.find_elements(By.CLASS_NAME, 'product-card__info')

print(len(infos))

# for info in infos:
#     # print(info.text)
#     title = info.find_element(By.CLASS_NAME, 'product-card__title').text
#     subtitle = info.find_element(By.CLASS_NAME, 'product-card__subtitle').text
#     price = info.find_element(By.CLASS_NAME, 'product-card__price').text
#     print(f'{title}/{subtitle} : {price}')
# driver.close()