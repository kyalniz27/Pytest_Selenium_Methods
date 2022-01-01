from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
import pytest

@pytest.mark.launchChromeBrowser
def test_chrome_browser():
    path = "C://Users//seker//Documents//driver//chromedriver.exe";
    driver = Chrome(executable_path=path)
    driver.get("https://www.amazon.com")
    print(driver.title)
    driver.close()

@pytest.mark.launchFirefoxBrowser
def test_firefox_browser():
    path = "C://Users//seker//Documents//driver//geckodriver.exe";
    driver = Firefox(executable_path=path)
    driver.get("https://www.amazon.com")
    print(driver.title)
    driver.close()




