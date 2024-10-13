from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config

class LoginPage(BasePage):
    # Locators
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, "/html/body/main/section/div[2]/form/button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)  # Navigate to the login page

    def enter_email(self, email):
        """Enter the email into the email input field."""
        self.input_text(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        """Enter the password into the password input field."""
        self.input_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def perform_login(self, email, password):
        """Perform login with email and password."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
