from time import sleep
from selenium.webdriver import Firefox, ActionChains
import pytest
from selenium.webdriver.common.by import By
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

def test_mouse_hover(setPath):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    #driver.execute_script("window.scrollBy(0,800)", "")
    time_machine = driver.find_element(By.CSS_SELECTOR, "#mousehover")
    driver.execute_script("arguments[0].scrollIntoView();",time_machine)

    sleep(2)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
    sleep(2)
    driver.find_element_by_css_selector("a[href='#top']").click()
    sleep(2)