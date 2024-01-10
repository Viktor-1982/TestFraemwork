from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

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
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла