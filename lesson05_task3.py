from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)



driver.maximize_window()  
sleep(2)  
    
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='number']"))
)

# Ввод текста "12345"
input_field.send_keys("12345")
print("Введено значение: 12345")
sleep(1)  

# Очистка поля
input_field.clear()
print("Поле очищено")
sleep(1) 

# Ввод текста "54321"
input_field.send_keys("54321")
print("Введено значение: 54321")
sleep(2)

driver.quit()