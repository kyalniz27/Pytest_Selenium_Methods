from selenium.webdriver import Firefox
import pytest
from time import sleep

from selenium.webdriver.support.select import Select


@pytest.fixture()
def setPath():
    global driver
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)


'''
def test_dropdown(setPath):
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    sleep(2)

    selectDay = Select(driver.find_element_by_id("day"))
    selectDay.select_by_index(20)
    sleep(2)
    selectMonth = Select(driver.find_element_by_id("month"))
    selectMonth.select_by_visible_text("Mar")
    sleep(2)
    selectYear = Select(driver.find_element_by_id("year"))
    selectYear.select_by_value("1985")

    driver.close()
'''


def test_rahul_dropdown(setPath):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    sleep(2)

    #driver.find_element_by_css_selector("#dropdown-class-example").click()
    select1 = Select(driver.find_element_by_css_selector("#dropdown-class-example"))
    select1.select_by_index(1)
    sleep(1)
    select2 = Select(driver.find_element_by_css_selector("#dropdown-class-example"))
    select2.select_by_value("Option2")
    sleep(1)
    select3 = Select(driver.find_element_by_css_selector("#dropdown-class-example"))
    select3.select_by_visible_text("Option3")
    sleep(1)



