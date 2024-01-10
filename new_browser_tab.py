from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:


    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)

    input1= browser.find_element(By.XPATH, '//button[@class ="btn btn-primary"]').click()
    time.sleep(7)

    alert = browser.switch_to.alert
    alert.accept()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()