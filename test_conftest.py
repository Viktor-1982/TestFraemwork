from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

def find_element1_on_the_page(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
