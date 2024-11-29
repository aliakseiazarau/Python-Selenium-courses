from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    frst_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    frst_name.send_keys('Petya')
    lst_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    lst_name.send_keys('Kakov')
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys('PetyaKakov@sobaka.com')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()