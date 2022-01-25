from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    picture = browser.find_element_by_id('treasure')
    x = picture.get_attribute('valuex')
    result = calc(x)
    text_area = browser.find_element_by_id('answer')
    text_area.send_keys(result)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_class_name('btn-default')
    button.click()
finally:
    time.sleep(5)
    browser.quit()