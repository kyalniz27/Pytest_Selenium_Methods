from time import sleep
from selenium.webdriver import Firefox, ActionChains
import pytest

@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_iFrame(setPath):
    driver.get("http://londonfreelance.org/courses/frames/index.html")

    driver.switch_to.frame(driver.find_element_by_name("main"))
    header = driver.find_element_by_css_selector("body > h2")
    print("\n", header.text )

    driver.switch_to.default_content()
    print(driver.title)