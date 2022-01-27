import unittest
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):
    def test1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input1.send_keys("Sergey")
        input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input2.send_keys("Makarenkov")
        input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input3.send_keys("123@321.net")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Ожидаемый текст не совпал с текущим!')

    def test2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input1.send_keys("Sergey")
        input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input2.send_keys("Makarenkov")
        input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input3.send_keys("123@321.net")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Ожидаемый текст не совпал с текущим!')

if __name__ == "__main__":
    unittest.main()