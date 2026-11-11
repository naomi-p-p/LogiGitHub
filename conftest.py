from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print(f"Driver:{driver}")
    yield driver
    driver.quit()  # runs even if the test fails