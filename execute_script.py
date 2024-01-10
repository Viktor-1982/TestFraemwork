from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находит "x" и получает это значение
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    x = x_element
    y = calc(x)

    # Вводит полученное по формуле значение
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    # Кликает radiobutton со значением "robotsRule"
    button = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # кликает Checkbox  со значением "I'm the robot"
    button1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    button1.click()

    # кликает кнопку Submit
    button2 = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    button2.click()
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
