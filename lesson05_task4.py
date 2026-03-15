from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
    
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window() 
time.sleep(2)  

   
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")
print("Логин введен: tomsmith")

    
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")
print("Пароль введен: SuperSecretPassword!")

    
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
print("Кнопка 'Login' нажата")
time.sleep(3)  

success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash"))
    )
print("Текст с зелёной плашки:", success_message.text)
    
driver.quit()