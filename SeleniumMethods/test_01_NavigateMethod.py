from selenium.webdriver import Firefox
import pytest
from time import sleep

@pytest.mark.launchFirefoxBrowser
def test_navigate_browser():
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)

    driver.get("https://www.amazon.com")
    print(driver.title)
    sleep(1)
    driver.get("https://www.youtube.com")
    print(driver.title)
    sleep(1)
    driver.forward()
    sleep(1)
    driver.back()
    sleep(1)
    driver.close()
    