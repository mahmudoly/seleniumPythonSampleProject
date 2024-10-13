import pytest
from pages.login_page import LoginPage
from utils.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.perform_login(Config.USER_NAME, Config.PASSWORD)

        # Wait for the element to be present after successful login
        welcome_message_locator = (By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/h2')
        welcome_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(welcome_message_locator)
        )

        # Assert that the text of the element is "Welcome"
        assert welcome_element.text == "Welcome", "Login failed or Welcome message not found!"
