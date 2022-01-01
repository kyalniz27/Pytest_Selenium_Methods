from selenium.webdriver import Firefox, ActionChains
import pytest
from time import sleep

@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)

def test_dragAndDrop(setPath):
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://demo.automationtesting.in/Static.html")

    source = driver.find_element_by_xpath("//img[@id='node']")
    target = driver.find_element_by_xpath("//div[@id='droparea']")

    action = ActionChains(driver)
    action.drag_and_drop(source,target).perform()

    sleep(2)
    driver.close()


    