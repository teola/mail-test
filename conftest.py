import pytest
import time
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    yield driver
    time.sleep(3)
    driver.quit()
