from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'https://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    # кликает на приветственное сообщение
    button = browser.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

    # принимает alert и соглашается
    alert = browser.switch_to.alert
    alert.accept()

    # находит элемент x и возвращает его значение. Высчитывает  формулу
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)

    input2 = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    # Чтобы получить текст из alert, используйте свойство text объекта alert
    # alert = browser.switch_to.alert
    # alert_text = alert.text

    # confirm - окно, где есть выбор действия
    #confirm = browser.switch_to.alert    # переключиться на окно с alert,
    #confirm.accept()                    # принять его с помощью команды accept

    # confirm = browser.switch_to.alert    # переключиться на окно с confirm
    # confirm.dismiss()     #      отменить confirm

    # если alert имеет дополнительное поле для ввода текста.Чтобы ввести текст
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()


finally:
    time.sleep(5)
    browser.quit()
