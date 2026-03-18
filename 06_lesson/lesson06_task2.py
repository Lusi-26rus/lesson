from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)

driver.get("http://uitestingplayground.com/textinput")

button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
button.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

but = driver.find_element(By.CSS_SELECTOR, ".form-group")
txt = but.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

driver.quit()



