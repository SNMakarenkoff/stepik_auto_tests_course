from selenium import webdriver
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_tag_name('button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value')
    x = int(x.text)
    result = calc(x)
    text_area = browser.find_element_by_id('answer')
    text_area.send_keys(result)
    button2 = browser.find_element_by_class_name('btn-primary')
    button2.click()
finally:
    time.sleep(7)
    browser.quit()