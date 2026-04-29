import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver):
        """Инициализация драйвера и локаторов."""
        self.driver = driver
        self.url = ("https://bonigarcia.dev/selenium-webdriver-java/"
                    "slow-calculator.html")
        self._delay_input = (By.ID, "delay")
        self._result_display = (By.CLASS_NAME, "screen")
        self._spinner = (By.ID, "spinner")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает URL страницы калькулятора."""
        self.driver.get(self.url)

    @allure.step("Установить задержку {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает значение задержки в поле ввода.
        :param seconds: Время задержки в секундах (строка).
        """
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    @allure.step("Нажать на кнопку '{text}'")
    def click_button(self, text: str) -> None:
        """
        Находит и кликает по кнопке калькулятора с указанным текстом.
        :param text: Текст на кнопке (цифра или оператор).
        """
        wait = WebDriverWait(self.driver, 10)
        xpath = f"//span[contains(@class, 'btn') and text()='{text}']"
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    @allure.step("Ожидание и получение результата вычислений")
    def get_result(self, timeout: int = 50) -> str:
        """
        Дожидается исчезновения спиннера и возвращает текст с экрана.
        :param timeout: Максимальное время ожидания (по умолчанию 50 сек).
        :return: Строка с результатом вычислений.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(self._spinner))
        return self.driver.find_element(*self._result_display).text
