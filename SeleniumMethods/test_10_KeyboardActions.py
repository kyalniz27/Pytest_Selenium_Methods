from time import sleep
from selenium.webdriver import Firefox
import pytest
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_google_search(setPath):
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("Python")
    sleep(2)
    driver.find_element_by_name("q").send_keys(Keys.ARROW_DOWN)
    sleep(2)
    driver.find_element_by_name("q").send_keys(Keys.ENTER)

def test_copy_paste(setPath):
    driver.maximize_window()
    driver.get("http://www.teachmeselenium.com/automation-practice")
    driver.find_element_by_id("firstname").send_keys("python")
    sleep(2)
    driver.find_element_by_id("firstname").send_keys(Keys.COMMAND, "a")
    sleep(2)
    driver.find_element_by_id("firstname").send_keys(Keys.COMMAND, "c")
    sleep(2)
    driver.find_element_by_id("firstname").send_keys(Keys.COMMAND, "v")
    sleep(2)