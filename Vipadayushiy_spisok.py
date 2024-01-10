from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  return (int(x)+int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищет значения элементов и суммирует их
    x = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    y = browser.find_element(By.XPATH, '//span[@id="num2"]').text
    z = calc(x,y)

    # выбирает элемент из выпадающего списка равный сумме значений предыдущих
    select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
    select.select_by_value(str(z))

    # кликает кнопку Submit
    input = browser.find_element(By.XPATH, '//*[@class="btn btn-default"]')
    input.click()
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
