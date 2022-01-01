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

