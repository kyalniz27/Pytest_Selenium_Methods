from selenium.webdriver import Firefox
import pytest
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def setUp():
    global driver
    opts = Options()
    opts.headless = True
    driver = Firefox(options=opts)
    driver.implicitly_wait(10)

def test_verify_title(setUp):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    assert driver.title == "Practice Page"


def test_autocomplete_wait(setPath):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    country = driver.find_element_by_css_selector("#autocomplete").text
    driver.find_element_by_css_selector("#autocomplete").send_keys("USA")
    driver.find_element_by_xpath("/html[1]/body[1]/ul[1]/li[1]/div[1]").click()
    print(country.text())
