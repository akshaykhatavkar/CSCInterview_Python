import pytest
from selenium import webdriver

@pytest.fixture
def driverManager():
    print("Setting up driver")
    driver = webdriver.Chrome()
    yield driver
    print("Performing teardown")
    driver.quit()