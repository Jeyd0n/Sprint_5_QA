import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators import Register, Login
from src.urls import Urls
from src.data import GeneratedData


class TestRegistration:

    def test_registration_correct_email(
        self, 
        driver
    ):
        driver.get(Urls.url_register)

        driver.find_element(*Register.register_name_field).send_keys(GeneratedData.name)
        driver.find_element(*Register.register_email_field).send_keys(GeneratedData.login)
        driver.find_element(*Register.register_password_field).send_keys(GeneratedData.password)

        driver.find_element(*Register.register_register_button).click()

        WebDriverWait(
            driver, 
            8
        ).until(
            EC.presence_of_element_located(Login.element_with_login_text)
        )

        login_button = driver.find_element(*Login.element_with_login_text)

        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'

    def test_registration_empty_name_nothing_happens(
        self, 
        driver
    ):
        driver.get(Urls.url_register)

        driver.find_element(*Register.register_email_field).send_keys(GeneratedData.name)
        driver.find_element(*Register.register_password_field).send_keys(GeneratedData.login)

        driver.find_element(*Register.register_register_button).click()

        WebDriverWait(
            driver, 
            5
        ).until(
            EC.element_to_be_clickable(Register.register_register_button)
        )
        time.sleep(2)

        errors_messages = driver.find_elements(*Register.register_error_message)

        assert driver.current_url == Urls.url_register and len(errors_messages) == 0


    @pytest.mark.parametrize(
        'email',
        [
            'pupa2@yanru', 'three3yan.ru', 'ya moscow3@yan.ru', 
            '8@ya n.ru', '@yan.ru', 'te6@.ru', 'tes7@yan.'
        ]
                                            
    )
    def test_registration_incorrect_email_show_error(
        self, 
        driver, 
        email
    ):
        driver.get(Urls.url_register)

        driver.find_element(*Register.register_name_field).send_keys('LeBron James')
        driver.find_element(*Register.register_email_field).send_keys(email)
        driver.find_element(*Register.register_password_field).send_keys('686765')

        driver.find_element(*Register.register_register_button).click()

        WebDriverWait(
            driver, 
            5
        ).until(
            EC.presence_of_element_located(Register.register_error_message_2)
        )
        error_message = driver.find_element(*Register.register_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize(
        'password', 
        [
            '1', '12345'
        ]
    )
    def test_login_incorrect_password_less_six_symbols_show_error(
        self, 
        driver, 
        password
    ):
        driver.get(Urls.url_register)

        driver.find_element(*Register.register_name_field).send_keys('Stephen Curry')
        driver.find_element(*Register.register_email_field).send_keys('pupka1@yan.ru')
        driver.find_element(*Register.register_password_field).send_keys(password)

        driver.find_element(*Register.register_register_button).click()

        WebDriverWait(
            driver, 
            5
        ).until(
            EC.presence_of_element_located(Register.register_error_message)
        )

        error_message = driver.find_element(*Register.register_error_message)

        assert error_message.text == 'Некорректный пароль'
        