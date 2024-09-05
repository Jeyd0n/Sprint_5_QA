import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import Main, Login
from src.urls import Urls
from src.data import Myself


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get(Urls.url_main_paige)

    yield driver

    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Urls.url_login)

    driver.find_element(*Login.login_email_field).send_keys(Myself.login)
    driver.find_element(*Login.login_password_field).send_keys(Myself.password)

    driver.find_element(*Login.login_button_any_forms).click()

    WebDriverWait(
        driver,
        3
    ).until(
        EC.presence_of_element_located(Main.main_order_button)
    )

    return driver
