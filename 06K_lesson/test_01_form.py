import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "first-name"))
    ).send_keys("Иван")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "last-name"))
    ).send_keys("Петров")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "address"))
    ).send_keys("Ленина, 55-3")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "e-mail"))
    ).send_keys("test@skypro.com")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "phone"))
    ).send_keys("+7985899998787")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "city"))
    ).send_keys("Москва")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "country"))
    ).send_keys("Россия")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "job-position"))
    ).send_keys("QA")

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "company"))
    ).send_keys("SkyPro")

    
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()
    def has_validation_class(element, expected_class):
        classes = element.get_attribute("class") or ""
        return expected_class in classes.split()

# Проверка zip-code
    zip_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
)
    assert has_validation_class(zip_input, "alert-danger"), "Zip code не подсвечен красным"

# Проверка остальных полей
    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
]

    for field in green_fields:
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, field))
    )
        assert has_validation_class(element, "alert-success"), f"Поле {field} не подсвечено зелёным"