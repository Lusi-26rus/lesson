import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс страницы авторизации."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-button")

    @allure.step("Авторизоваться пользователем {user}")
    def login(self, user: str, pwd: str) -> None:
        """
        Вводит логин, пароль и нажимает кнопку входа.
        :param user: Имя пользователя.
        :param pwd: Пароль.
        """
        self.driver.find_element(*self._username).send_keys(user)
        self.driver.find_element(*self._password).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()


class InventoryPage:
    """Класс страницы каталога товаров."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._items = {
            "Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар '{item_key}' в корзину")
    def add_item_to_cart(self, item_key: str) -> None:
        """
        Нажимает кнопку добавления в корзину для указанного товара.
        :param item_key: Ключ товара из словаря self._items.
        """
        self.driver.find_element(*self._items[item_key]).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Нажимает на иконку корзины."""
        self.driver.find_element(*self._cart_link).click()


class CartPage:
    """Класс страницы корзины."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(*self._checkout_btn).click()


class CheckoutPage:
    """Класс страницы оформления заказа и проверки данных."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zip_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму данными: {first} {last}, индекс: {zip_code}")
    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет данные покупателя и нажимает Continue.
        :param first: Имя.
        :param last: Фамилия.
        :param zip_code: Почтовый индекс.
        """
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    @allure.step("Получить итоговую стоимость")
    def get_total_price(self) -> str:
        """
        Считывает итоговую сумму с финальной страницы.
        :return: Строка вида 'Total: $XX.XX'.
        """
        return self.driver.find_element(*self._total_label).text
