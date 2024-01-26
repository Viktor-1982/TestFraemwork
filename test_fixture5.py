import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize("url", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_feedback_message(browser, url):
    browser.get(url)
    answer = math.log(int(time.time()))
    input_field = browser.find_element_by_css_selector("textarea")
    input_field.send_keys(str(answer))
    submit_button = browser.find_element(By.C)             ("button.submit-submission")
    submit_button.click()
    feedback = browser.find_element_by_css_selector("pre.smart-hints__hint")
    assert feedback.text == "Correct!", f"Expected 'Correct!' in feedback, but got '{feedback.text}'"
