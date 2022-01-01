from selenium.webdriver import Firefox
import pytest

@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)


def test_assertion_method(setPath):
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    actTitle = driver.title
    assert actTitle == "Practice Page"
    driver.quit()