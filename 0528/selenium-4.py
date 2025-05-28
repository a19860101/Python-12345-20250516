from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'

driver.get(url)
driver.maximize_window()

# product-card__titles

# titles = driver.find_elements(By.CLASS_NAME, 'product-card__title')
# titles = driver.find_elements(By.XPATH, '//*[@id="skip-to-products"]/div[2]/div/figure/div/div/div')
# print(titles)
# By.TAG_NAME
# By.CLASS_NAME
# By.ID
# By.NAME
# BY.XPATH


# for title in titles:
#     print(title.text)

infos = driver.find_elements(By.CLASS_NAME, 'product-card__info')

for info in infos:
    # print(info.text)
    title = info.find_element(By.CLASS_NAME, 'product-card__title').text
    subtitle = info.find_element(By.CLASS_NAME, 'product-card__subtitle').text
    price = info.find_element(By.CLASS_NAME, 'product-card__price').text
    print(f'{title}/{subtitle} : {price}')

driver.close()