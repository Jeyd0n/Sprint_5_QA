from src.locators import Main


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_constructor_button).click()
        driver.find_element(*Main.main_sauces_button).click()

        h_sauce = driver.find_element(*Main.main_h_sauces)

        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_constructor_button).click()
        driver.find_element(*Main.main_filling_button).click()
        h_filling = driver.find_element(*Main.main_h_filling)

        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(
        self, 
        login
    ):
        driver = login

        driver.find_element(*Main.main_constructor_button).click()
        driver.find_element(*Main.main_filling_button).click()
        driver.find_element(*Main.main_ban_button).click()

        h_ban = driver.find_element(*Main.main_h_ban)

        assert h_ban.text == 'Булки'