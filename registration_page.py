from .base_page import BasePage
from .locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    """Класс для работы со страницей регистрации"""

    def enter_first_name(self, first_name):
        """Ввод имени пользователя"""
        first_name_field = self.find_element(*RegistrationPageLocators.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        """Ввод фамилии пользователя"""
        last_name_field = self.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        """Ввод email пользователя"""
        email_field = self.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Ввод пароля пользователя"""
        password_field = self.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def confirm_password(self, password):
        """Подтверждение пароля"""
        confirm_password_field = self.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)

    def click_register_button(self):
        """Нажатие на кнопку регистрации"""
        register_button = self.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()
