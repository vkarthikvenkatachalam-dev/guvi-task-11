import pytest
from selenium import webdriver


@pytest.fixture
def start_browser():
    driver = webdriver.Edge()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    return driver
