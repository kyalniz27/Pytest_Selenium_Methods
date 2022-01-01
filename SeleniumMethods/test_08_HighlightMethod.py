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

def test_highlihhted_element(setPath):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    element = driver.find_element_by_css_selector("#autocomplete")
    element.send_keys("USA")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html[1]/body[1]/ul[1]/li[1]/div[1]")))
    driver.find_element_by_xpath("/html[1]/body[1]/ul[1]/li[1]/div[1]").click()

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                          "background: yellow; border: 3px solid red;")


def test_login_invalid_data(setPath):
    driver.get("https://app.hubspot.com/login")
    sleep(5)
    driver.maximize_window()
    username = driver.find_element_by_id("username")
    add_highlight(username)
    username.send_keys("sammy@sample.com")
    sleep(2)
    password = driver.find_element_by_id("password")
    add_highlight(password)
    password.send_keys("test12345")
    sleep(2)
    login = driver.find_element_by_id("loginBtn")
    add_highlight(login)
    login.click()
    sleep(2)


def add_highlight(element):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                          "background: yellow; border: 3px solid red;")