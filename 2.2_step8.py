from selenium import webdriver
import os, time

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('Sergey')
    soname = browser.find_element_by_css_selector('[name="lastname"]')
    soname.send_keys('Makarenkov')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('123@123.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2.2_step8.txt')           # добавляем к этому пути имя файла
    load_file = browser.find_element_by_id('file')
    load_file.send_keys(file_path)
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

