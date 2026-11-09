import pytest
from selenium import webdriver




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # runs even if the test fails




def test_google_title(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"