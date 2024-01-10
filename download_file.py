from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    file_path = ('file.txt')
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    # заполняет формы
    input1 = browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys("Ivanov")
    input3 = browser.find_element(By.XPATH, '//input[@name="email"]').send_keys("dfef.@mail.ru")

    button = browser.find_element(By.XPATH, '//input[@name="file"]')     # находит кнопку "Загрузить"
    current_dir = os.path.abspath(os.path.dirname(__file__))        # путь к директории
    file_path = os.path.join(current_dir, 'file.txt')               # добавляем к этому пути имя файла
    button.send_keys(file_path)                                     # загружает файл

    # кликает Submit
    input4 = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
