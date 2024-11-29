from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return num1 + num2
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    x = str(int(num1) + int(num2))
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdown.select_by_value(x)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    time.sleep(20)
    browser.quit()