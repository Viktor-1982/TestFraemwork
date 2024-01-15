from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

class Test_Abs(unittest.TestCase):
    def test_1(self):

      browser.get(link1)

    # находит элемент "First name" и вводит значение
      input1 = browser.find_element(By.XPATH, '//input[@class="form-control first"][1]')
      input1.send_keys("Viktor")

    # находит элемент "Last name" и вводит значение
      input2 = browser.find_element(By.XPATH, '//input[@class="form-control second"]')
      input2.send_keys("Ivanov")

    # находит элемент "Email" и вводит значение
      input3 = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
      input3.send_keys("ivssdh@mail.ru")

    # находит элемент "Phone" и вводит значение
      input4 = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
      input4.send_keys("7774899499400")

    # находит элемент "Address" и вводит значение
      input5 = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
      input5.send_keys("Moscow")

    # находит кнопку "Submit" и кликает её
      button = browser.find_element(By.CSS_SELECTOR, "button.btn")
      button.click()

      time.sleep(4)

    # находим элемент, содержащий текст
      welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
      welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    # успеваем скопировать код за 30 секунд
      time.sleep(6)
    # закрываем браузер после всех манипуляций
      browser.quit()

    def test_2(self):   # Тест упадет!!!

        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        ...

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()

  ##   Команды для Pytest
# pytest scripts/selenium_scripts
# # найти все тесты в директории scripts/selenium_scripts
#
# pytest test_user_interface.py
# # найти и выполнить все тесты в файле
#
# pytest scripts/drafts.py::test_register_new_user_parametrized
# # найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

# Если запустить PyTest с параметром -v (verbose, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения: