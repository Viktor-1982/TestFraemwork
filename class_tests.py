import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time




@pytest.fixture()

link = "http://suninjuly.github.io/registration1.html"
def browser():
  browser = webdriver.Chrome()
  browser.implicitly_wait(10)
  return browser

def input1(browser):
  browser.get(link)
  assert browser.find_element(By.XPATH, '//input[@class="form-control first"][1]').send_keys("Ivan")


def input2(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, '//input[@class="form-control second"]').send_keys("Ivanov")

def input3(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, '//input[@class="form-control third"]').send_keys("fdfd@mail.ru")

def input4(browser):
     browser.get(link)
     assert browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]').send_keys("+8845845845848")

def input5(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]').send_keys("Moscow")

def input6(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn").click()


        # находит кнопку "Submit" и кликает её
def button(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()