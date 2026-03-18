from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
# driver.get("http://uitestingplayground.com/visibility") #переход на сайт

# #проверка видимости кнопки Opacity 0
# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed() 

# print(is_displayed) #вывод статуса видимости Opacity 0

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click() #нажатие на Hide
# # Opacity 0 окажется скрытой
# sleep(2)

# #еще раз проверим видимость Opacity 0:
# is_displayed = driver.find_element(
# By.CSS_SELECTOR, "#transparentButton").is_displayed()

# print(is_displayed) #еще раз выводим статус видимости Opacity 0

# sleep(2)


# driver.get("https://demoqa.com/radio-button")
# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)
# driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")

# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# cb.click()
# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

driver.get("https://the-internet.herokuapp.com/checkboxes")
# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR, "a")
# print (a.get_attribute("href"))

divs = driver.find_elements(By.CSS_SELECTOR, "div")

# l = len(divs)
# print(l)


div = divs[6]
css_class = div.get_attribute("class")
print(css_class)
driver.quit()