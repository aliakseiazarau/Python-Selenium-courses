from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    frst_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"')
    frst_name.send_keys('Petya')
    lst_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lst_name.send_keys('Kakov')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('PetyaKakov@sobaka.com')
    file_load = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_load.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

