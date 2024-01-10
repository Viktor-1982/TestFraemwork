from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находит картинку со скрытым значением и получает это значение

    x_element = browser.find_element(By.XPATH, '//img[@id="treasure"]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    input2 = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    input2.click()
    input3 = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    input3.click()

    input4 = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')
    input4.click()

    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
