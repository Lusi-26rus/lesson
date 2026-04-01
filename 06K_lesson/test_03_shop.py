import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_shopping_process(driver):
   
    driver.get("https://www.saucedemo.com/")

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    
    backpack_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Backpack']/following::button[1]"))
    )
    backpack_add_button.click()

    tshirt_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/following::button[1]"))
    )
    tshirt_add_button.click()

    onesie_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Onesie']/following::button[1]"))
    )
    onesie_add_button.click()

    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_icon.click()

    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Иванов")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )
    total_text = total_element.text

    total_amount = float(total_text.split("$")[1])

    print(f"Итоговая сумма: ${total_amount}")

    expected_total = 58.29
    assert abs(total_amount - expected_total) < 0.01, (
        f"Ожидаемая сумма: ${expected_total}, но получено: ${total_amount}"
    )
