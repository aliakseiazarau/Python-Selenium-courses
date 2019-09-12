import unittest


# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#     from selenium import webdriver
#     import time


class unittest1(unittest.TestCase):
    def test_registration1


# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_css_selector(".first_block .first")
#     input1.send_keys("Pipi")
#     input2 = browser.find_element_by_css_selector(".first_block .second")
#     input2.send_keys("SyuSyu")
#     input3 = browser.find_element_by_css_selector(".first_block .third")
#     input3.send_keys("Pipisyusyu@mail.comfwd")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     time.sleep(1)
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     welcome_text = welcome_text_elt.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(10)
#     browser.quit()