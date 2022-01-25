from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    var_x = browser.find_element_by_id('input_value')
    x = var_x.text
    result = calc(x)
    input_text = browser.find_element_by_css_selector('[type="text"]')
    input_text.send_keys(result)
    check_robot = browser.find_element_by_id('robotCheckbox')
    check_robot.click()
    radio_robot = browser.find_element_by_id('robotsRule')
    radio_robot.click()
    sumbit_button = browser.find_element_by_class_name('btn-default')
    sumbit_button.click()
finally:
    time.sleep(5)
    browser.quit()
