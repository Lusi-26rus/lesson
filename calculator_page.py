from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей медленного калькулятора."""

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self._delay_input = (By.ID, "delay")
        self._result_display = (By.CLASS_NAME, "screen")
        self._spinner = (By.ID, "spinner")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text):
        wait = WebDriverWait(self.driver, 10)
        # Ищем кнопку по тексту напрямую через XPath для надежности
        xpath = f"//span[contains(@class, 'btn') and text()='{text}']"
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    def get_result(self, timeout=50): # Добавили значение по умолчанию
        wait = WebDriverWait(self.driver, timeout)
        # Ждем исчезновения спиннера
        wait.until(EC.invisibility_of_element_located(self._spinner))
        # Возвращаем результат для ассерта в тесте
        return self.driver.find_element(*self._result_display).text