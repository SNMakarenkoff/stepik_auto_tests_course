import pytest
import math, time
from selenium import webdriver



@pytest.fixture(scope='function')
def browser():
    print('\nStart browser for test...')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print('\nQuit browser...')
    browser.quit()

@pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_enter_answer(browser, link):
    link = f'https://stepik.org/lesson/{link}/step/1'
    browser.get(link)
    text_area = browser.find_element_by_tag_name('textarea')
    answer = str(math.log(int(time.time())))
    text_area.send_keys(answer)
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    fidback = browser.find_element_by_css_selector('.smart-hints__hint')
    assert fidback.text == 'Correct!', 'Текст фидбэка не совпадает с ожидаемым - Correct!'
