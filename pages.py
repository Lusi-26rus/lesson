from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-button")

    def login(self, user, pwd):
        self.driver.find_element(*self._username).send_keys(user)
        self.driver.find_element(*self._password).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        
        self._items = {
            "Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_key):
        self.driver.find_element(*self._items[item_key]).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    def checkout(self):
        self.driver.find_element(*self._checkout_btn).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zip_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    def get_total_price(self):
        
        total_text = self.driver.find_element(*self._total_label).text
        return total_text