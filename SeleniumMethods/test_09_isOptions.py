from time import sleep
from selenium.webdriver import Firefox
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_isOptions_methods(setPath):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    hideShow = driver.find_element_by_css_selector("#displayed-text")
    print(hideShow.is_displayed())
    driver.find_element_by_css_selector("#hide-textbox").click()
    print(hideShow.is_displayed())


    