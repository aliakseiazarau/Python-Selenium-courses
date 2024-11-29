import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('url', links)
def test_check_modal(browser, load_config, url):
    browser.get(url)
    login = load_config["login_stepik"]
    password = load_config["password_stepik"]
    time.sleep(2)
    login_button = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    login_button.click()
    login_field = browser.find_element(By.ID, "id_login_email")
    login_field.send_keys(login)
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys(password)
    confirm_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    confirm_button.click()
    WebDriverWait(browser, 5).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-dialog__content")), 5)
    # WebDriverWait(browser, 5).until_not(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog__content")), 5)
    answer = math.log(int(time.time()))
    time.sleep(3)
    textarea = browser.find_element(By.CLASS_NAME, "ember-text-area")
    textarea.send_keys(answer)
    send_button = browser.find_element(By. CLASS_NAME, "submit-submission")
    send_button.click()
    result = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")), 5)
    assert result.text == "Correct!", "Answer is incorrect!"
    
