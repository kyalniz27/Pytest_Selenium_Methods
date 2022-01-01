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

def test_right_click(setPath):
    driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    action = ActionChains(driver)
    action.context_click(driver.find_element_by_xpath("//span[text()='right click me']")).perform()
    sleep(2)

    driver.find_element_by_xpath("//ul[@class='context-menu-list context-menu-root']/li[3]").click()
    sleep(2)

    obj = driver.switch_to.alert
    msg = obj.text
    print(msg)
    sleep(2)
    obj.accept()