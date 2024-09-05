from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.locators import Main, Profile, Login
from src.urls import Urls


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_profile_button).click()
        WebDriverWait(
            driver, 
            3
        ).until(
            EC.presence_of_element_located(Profile.info_message)
        )
        
        profile = driver.find_element(*Profile.history_shop_button)

        assert Urls.url_profile == driver.current_url and profile.text == 'История заказов'

    def test_click_constructor_button_show_constructor_form(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_profile_button).click()
        WebDriverWait(
            driver, 
            3
        ).until(
            EC.presence_of_element_located(Profile.info_message)
        )

        driver.find_element(*Main.main_constructor_button).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")

        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_profile_button).click()
        WebDriverWait(
            driver, 
            3
        ).until(
            EC.presence_of_element_located(Profile.info_message)
        )

        driver.find_element(*Main.main_logo).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")

        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

        driver = login

        driver.find_element(*Main.main_profile_button).click()
        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Profile.info_message)
        )

        driver.find_element(*Profile.logout_button).click()
        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.login_button_any_forms)
        )

        login_button = driver.find_element(*Login.element_with_login_text)

        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'
        