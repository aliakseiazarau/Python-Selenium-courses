from selenium import webdriver
import time
import math
import pytest



links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('url', links)
def test_ufo_message(browser, url):
    browser.get(url)
    answer = math.log(int(time.time()))
    time.sleep(3)
    pole = browser.find_element_by_tag_name("textarea")
    pole.send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission ").click()
    time.sleep(3)
    compare = browser.find_element_by_class_name("smart-hints__hint").text
    assert compare in "Correct!"


