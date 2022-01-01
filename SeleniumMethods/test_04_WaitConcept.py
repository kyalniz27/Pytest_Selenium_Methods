from selenium.webdriver import Firefox
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)


def test_explicitly_wait(setPath):
    driver.maximize_window()
    #driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    country = driver.find_element_by_css_selector("#autocomplete").text
    driver.find_element_by_css_selector("#autocomplete").send_keys("USA")
    WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"/html[1]/body[1]/ul[1]/li[1]/div[1]")))
    driver.find_element_by_xpath("/html[1]/body[1]/ul[1]/li[1]/div[1]").click()

    if country != None:
        print("It's there")
    else:
        assert False




    driver.quit()









