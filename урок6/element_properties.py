from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")


txt = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').text
tag = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').tag_name
id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').id
href = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').get_attribute ("href")
ff = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').value_of_css_property("font-family")
color = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.300000000101470118"]').value_of_css_property("color")

print (txt)
print(tag)
print(id)
print(href)
print(ff)
print(color)

sleep(10)

driver.quit()
