from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение 12 секунд, пока значение не станет $100
  price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
  # кликаем кнопку "book"
  button = browser.find_element(By.ID, "book").click()

  # находим значение x и высчитываем формулу из функции "calc"
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)

  # вводим полученое значение в поле
  input = browser.find_element(By.ID, "answer").send_keys(y)
  # кликаем на кнопку "Submit"
  button1  = browser.find_element(By.ID, "solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()