from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    num1 = num1.text
    num2 = browser.find_element_by_id('num2')
    num2 = num2.text
    value = int(num1) + int(num2)
    value = str(value)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(value)
    button = browser.find_element_by_class_name('btn-default')
    button.click()
finally:
    time.sleep(5)
    browser.quit()