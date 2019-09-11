from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os


# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# link = "http://suninjuly.github.io/find_link_text"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     time.sleep(5)
#     link1 = browser.find_element_by_link_text("224592")
#     link1.click()
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#        element.send_keys("Pipi")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()


# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath('//button[text()="Submit"]')
#     button.click()

# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element_by_css_selector(".first_block .first")
#     input1.send_keys("Pipi")
#     input2 = browser.find_element_by_css_selector(".first_block .second")
#     input2.send_keys("SyuSyu")
#     input3 = browser.find_element_by_css_selector(".first_block .third")
#     input3.send_keys("Pipisyusyu@mail.comfwd")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# link = "http://suninjuly.github.io/math.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y)
#
#     checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
#     radio = browser.find_element_by_css_selector("[for='robotsRule']").click()
#     button = browser.find_element_by_css_selector("[type='submit']")
#     button.click()

# link = "http://suninjuly.github.io/get_attribute.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_element = browser.find_element_by_id("treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y)
#
#     checkbox = browser.find_element_by_id("robotCheckbox").click()
#     radio = browser.find_element_by_id("robotsRule").click()
#     button = browser.find_element_by_css_selector("[type='submit']").click()


# link = "http://suninjuly.github.io/selects1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element_by_css_selector("span#num1").text
#     y = browser.find_element_by_css_selector("span#num2").text
#     z = int(x) + int(y)
#     a = str(z)
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value(a)
#     button = browser.find_element_by_css_selector("[type='submit']").click()


# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser.get(link)
#
#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))
#
#     element = browser.find_element_by_id("input_value").text
#     print(element)
#     x = int(element)
#     y = calc(x)
#     input = browser.find_element_by_id("answer")
#     browser.execute_script("arguments[0].scrollIntoView()", input)
#     input.send_keys(y)
#     checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
#     radio = browser.find_element_by_css_selector("[for='robotsRule']").click()
#     button = browser.find_element_by_css_selector("[type='submit']").click()
#
#     assert True
#     # button = browser.find_element_by_tag_name("button")
#     # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     # button.click()
#     # browser.execute_script("window.scrollBy(0, 40);")


# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/file_input.html"
#     browser.get(link)
#
#     input1 = browser.find_element_by_name("firstname")
#     input1.send_keys("Pipi")
#     input2 = browser.find_element_by_name("lastname")
#     input2.send_keys("SyuSyu")
#     input3 = browser.find_element_by_name("email")
#     input3.send_keys("Pipisyusyu@mail.comfwd")
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#     load = browser.find_element_by_css_selector("[type='file']")
#     load.send_keys(file_path)
#     button = browser.find_element_by_css_selector("[type='submit']").click()

# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser.get(link)
#     button = browser.find_element_by_css_selector("[type='submit']")
#     button.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))
#
#     element = browser.find_element_by_id("input_value").text
#     x = int(element)
#     y = calc(x)
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y)
#     button.click()

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    element1 = browser.find_element_by_id("input_value").text
    x = int(element1)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    # browser.find_element_by_css_selector("[type='submit']").click()
    time.sleep(2)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
