import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()

    # Устанавливаем задержку
    calc_page.set_delay("45")

    # Выполняем действия
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Получаем результат (внутри метода должно быть явное ожидание до 50 сек)
    result = calc_page.get_result()
    
    # Проверка вынесена из класса страницы в тест
    assert result == "15"