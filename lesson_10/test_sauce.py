import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.title("Покупка товаров в SauceDemo")
@allure.description("Тест проверяет полный цикл: лог ин, добавление 3-х товаров и проверку финальной цены.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_sauce_demo_purchase(driver):
    with allure.step("Открыть сайт SauceDemo"):
        driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Backpack")
    inventory_page.add_item_to_cart("Bolt T-Shirt")
    inventory_page.add_item_to_cart("Onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Ivan", "Ivanov", "123456")

    with allure.step("Проверка итоговой стоимости"):
        total = checkout_page.get_total_price()
        expected_total = "Total: $58.29"
        assert total == expected_total, (
            f"Ожидалось '{expected_total}', но получено '{total}'"
        )
