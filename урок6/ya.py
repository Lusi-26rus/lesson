from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
browser = webdriver.Firefox()


ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
chrome = webdriver.Chrome (service=ChromeService(ChromeDriverManager().install()))

def make_screenshot (browser):
    browser.maximize_window()
    browser.get("https://ya.ru/")
    sleep (5)

    browser.save_screenshot("./ya_"+browser.name+".png")
    browser.quit()

make_screenshot(chrome)
make_screenshot(ff)


