from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import Main, Login, Password
from src.urls import Urls
from src.data import Myself


class TestStellarBurgersLoginLogoutForm:

    def test_login_correct_email_and_password_show_main_page(
        self, 
        login
    ):
        driver = login

        order_button = driver.find_element(*Main.main_order_button)

        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_sign_in_button_show_login_page(
        self, 
        driver
    ):

        driver.find_element(*Main.main_auth).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.login_text)
        )

        driver.find_element(*Login.login_email_field).send_keys(Myself.login)
        driver.find_element(*Login.login_password_field).send_keys(Myself.password)

        driver.find_element(*Login.login_button_any_forms).click()

        WebDriverWait(
            driver, 
            5
        ).until(
            EC.presence_of_element_located(Main.main_order_button)
        )

        order_button = driver.find_element(*Main.main_order_button)

        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_personal_account_button_show_login_page(
        self,
        driver
    ):

        driver.find_element(*Main.main_profile_button).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.login_text)
        )

        driver.find_element(*Login.login_email_field).send_keys(Myself.login)
        driver.find_element(*Login.login_password_field).send_keys(Myself.password)

        driver.find_element(*Login.login_button_any_forms).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Main.main_order_button)
        )

        order_button = driver.find_element(*Main.main_order_button)

        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_registration_form_sign_in_button(
        self, 
        driver
    ):
        driver.get(Urls.url_register)

        driver.find_element(*Login.login_text_with_href).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.login_text)
        )

        driver.find_element(*Login.login_email_field).send_keys(Myself.login)
        driver.find_element(*Login.login_password_field).send_keys(Myself.password)

        driver.find_element(*Login.login_button_any_forms).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Main.main_order_button)
        )

        order_button = driver.find_element(*Main.main_order_button)

        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

    def test_login_forgot_password_form_sign_in_button(
        self, 
        driver
    ):
        driver.get(Urls.url_forgot_password)

        driver.find_element(*Password.login_text_with_href).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.login_text)
        )

        driver.find_element(*Login.login_email_field).send_keys(Myself.login)
        driver.find_element(*Login.login_password_field).send_keys(Myself.password)

        driver.find_element(*Login.login_button_any_forms).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Main.main_order_button)
        )

        order_button = driver.find_element(*Main.main_order_button)

        assert driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'
        