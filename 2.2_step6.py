from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element_by_id('input_value')
    x = int(x.text)
    result = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    text_area = browser.find_element_by_id('answer')
    text_area.send_keys(result)
    checkbox = browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button.click()
finally:
    time.sleep(5)
    browser.quit()
