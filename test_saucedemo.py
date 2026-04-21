import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_sauce_demo_purchase(driver):
    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавление товаров
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Backpack")
    inventory_page.add_item_to_cart("Bolt T-Shirt")
    inventory_page.add_item_to_cart("Onesie")

    # 4. Переход в корзину
    inventory_page.go_to_cart()

    # 5. Checkout
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 6. Заполнение формы
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Ivan", "Ivanov", "123456")

    # 7. Чтение итоговой стоимости
    total = checkout_page.get_total_price()

    # 8. Проверка (логика вынесена из Page Object в тест)
    assert total == "Total: $58.29"