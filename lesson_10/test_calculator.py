import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера Chrome."""
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.id("CALC-01")
@allure.title("Проверка работы медленного калькулятора")
@allure.description("Сложение 7 и 8 с установленной задержкой 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay("45")

    with allure.step("Ввод выражения: 7 + 8"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Проверка итогового результата"):
        result = calc_page.get_result()
        assert result == "15", f"Ожидалось 15, но получено {result}"
