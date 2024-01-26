import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import math


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_authoriz_on_stepik(browser, link):
    browser.get(link)

    browser.find_element(By.XPATH, "//*[@id='ember33']").click()
    print("clicking on 'Enter' element")
    browser.find_element(By.XPATH, "//*[@id='id_login_email']").send_keys("vles8878@gmail.com")
    print("input login")
    browser.find_element(By.XPATH, "//*[@id='id_login_password']").send_keys("asarhaddon1982")
    print("input password")
    time.sleep(3)
    browser.find_element(By.XPATH, "//*[@class='sign-form__btn button_with-loader ']").click()
    print("click enter")
    time.sleep(8)

    answer = math.log(int(time.time()-1.1))
    value_int = browser.find_element(By.XPATH, "//*[@class='ember-text-area ember-view textarea string-quiz__textarea']").send_keys(str(answer))
    time.sleep(2)
    browser.find_element(By. XPATH, "//*[@class='submit-submission']").click()
    print("clicked submit")
    time.sleep(8)
    feadback = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
    assert feadback.text == "Correct!"
    value_int.clear()

   #  print("enter value answer")
   ## browser.find_element(By.XPATH, "//*[@class='submit-submission']").click()
   #print("click 'send'")
    time.sleep(6)

  # pytest -s -v --browser_name=chrome test_stepik_3_6.py     Для запуска тестов на Сrome
  # pytest -s -v --browser_name=firefox test_stepik_3_6.py     Для запуска тестов на Firefox
  