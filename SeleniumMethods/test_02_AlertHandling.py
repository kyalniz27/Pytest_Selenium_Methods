from selenium.webdriver import Firefox
import pytest
from time import sleep

path = "C://Users//seker//Documents//driver//geckodriver.exe";
driver = Firefox(executable_path=path)

@pytest.mark.launchFirefoxBrowser
def test_navigate_browser():

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    driver.find_element_by_xpath("//input[@id='name']").send_keys("Mustafa")
    driver.find_element_by_css_selector("#confirmbtn").click()
    sleep(2)

    alert_handling()
    driver.close()

def alert_handling():
    obj = driver.switch_to.alert
    assert obj.text == "Hello Mustafa, Are you sure you want to confirm?"
    obj.accept()


