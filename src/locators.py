from selenium.webdriver.common.by import By


class Main:

    main_profile_button = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']"
    )
    main_auth = (
        By.XPATH,
        ".//button[text()='Войти в аккаунт']"
    )
    main_order_button = (
        By.XPATH,
        ".//button[text()='Оформить заказ']"
    )
    main_constructor_button = (
        By.XPATH,
        ".//p[text()='Конструктор']"
    )
    main_logo = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']"
    )

    main_sauces_button = (
        By.XPATH,
        ".//span[text()='Соусы']/parent::*"
    )
    main_h_sauces = (
        By.XPATH,
        ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    )

    main_ban_button = (
        By.XPATH,
        ".//span[text()='Булки']/parent::*"
    )
    main_h_ban = (
        By.XPATH,
        ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    )

    main_filling_button = (
        By.XPATH,
        ".//span[text()='Начинки']/parent::*"
    )
    main_h_filling = (
        By.XPATH,
        ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"
    )


class Login:

    login_text = (
        By.XPATH, ".//h2[text()='Вход']"
    )
    login_button_any_forms = (
        By.XPATH, ".//button[text()='Войти']"
    )
    login_text_with_href = (
        By.XPATH, ".//a[text()='Войти']"
    )
    alogin_button = (
        By.CLASS_NAME, "Auth_link__1fOlj"
    )
    login_email_field = (
        By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
    )
    login_password_field = (
        By.XPATH, ".//input[@type='password' and @name='Пароль']"
    )
    element_with_login_text = (
        By.XPATH, ".//*[text() = 'Вход']"
    )


class Register:

    register_name_field = (
        By.XPATH, 
        ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']"
    )
    register_email_field = (
        By.XPATH, 
        ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
    )
    register_password_field = (
        By.XPATH, 
        ".//input[@type='password' and @name='Пароль']"
    )
    register_register_button = (
        By.XPATH, 
        ".//button[text()='Зарегистрироваться']"
    )
    register_error_message = (
        By.XPATH, 
        ".//p[contains(@class, 'input__error')]"
    )
    register_error_message_2 = (
        By.XPATH, 
        ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']"
    )
    register_login_button = (
        By.CLASS_NAME,
        "Auth_link__1fOlj"
    )


class Password:

    login_text_with_href = (
        By.XPATH,
        ".//a[text()='Войти']"
    )


class Profile:
    
    logout_button = (
        By.XPATH,
        ".//button[text()='Выход']"
    )
    info_message = (
        By.XPATH,
        ".//p[contains(text(),'персональные данные')]"
    )
    history_shop_button = (
        By.XPATH,
        ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"
    )
    