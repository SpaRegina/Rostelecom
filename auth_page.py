from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AuthPage(BasePage):

    def select_phone_tab(self):
        """Выбор вкладки 'Телефон' для авторизации по номеру телефона."""
        phone_tab = self.find_element(*AuthPageLocators.PHONE_TAB)
        phone_tab.click()

    def select_login_tab(self):
        """Выбор вкладки 'Логин' для авторизации по логину или почте."""
        login_tab = self.find_element(*AuthPageLocators.LOGIN_TAB)
        login_tab.click()

    def enter_email_or_phone(self, email_or_phone):
        """Ввод email или номера телефона."""
        login_field = self.wait_for_element(AuthPageLocators.LOGIN_INPUT)
        login_field.clear()
        login_field.send_keys(email_or_phone)

    def enter_password(self, password):
        """Ввод пароля."""
        password_field = self.find_element(*AuthPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Нажатие на кнопку 'Войти'."""
        login_button = self.find_element(*AuthPageLocators.BTN_LOGIN)
        login_button.click()

    def get_error_message(self):
        """Получение сообщения об ошибке после неудачной попытки авторизации."""
        error_message = self.wait_for_element(AuthPageLocators.ERROR_MESSAGE)
        return error_message.text

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def click_register_link(self):
        """Нажимаем на ссылку перехода на страницу регистрации."""
        register_link = self.find_element(*AuthPageLocators.REGISTER_LINK)
        register_link.click()

    def enter_phone_number(self, phone_number):
        """Ввод номера телефона."""
        phone_input = self.find_element(By.ID, "address")
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def click_get_code_button(self):
        """Нажимаем кнопку для получения кода."""
        get_code_button = self.find_element(By.ID, "otp_get_code")
        get_code_button.click()

    def is_code_input_form_displayed(self):
        """Проверка, отображена ли форма для ввода кода."""
        return self.wait_for_element((By.ID, "card-title"))

    def enter_temporary_code(self, code):
        """Ввод временного кода."""
        code_input = self.find_element(By.ID, "rt-code-input")
        code_input.clear()
        code_input.send_keys(code)

    def is_cookie_disabled_message_displayed(self):
        """Проверка отображения сообщения о необходимости включения cookie."""
        try:
            return self.find_element(By.XPATH, "//*[contains(text(), 'Включите файлы cookie для продолжения')]").is_displayed()
        except NoSuchElementException:
            return False

    def enter_sms_code(self, code):
        sms_code_input = self.find_element(By.ID, "rt-code-input")
        sms_code_input.clear()
        sms_code_input.send_keys(code)

    def click_next_button(self):
        next_button = self.find_element(By.ID, "next_button")
        next_button.click()

    def enter_new_password(self, new_password):
        new_password_input = self.find_element(By.ID, "new_password")
        new_password_input.clear()
        new_password_input.send_keys(new_password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_input = self.find_element(By.ID, "confirm_password")
        confirm_password_input.clear()
        confirm_password_input.send_keys(confirm_password)

    def click_save_button(self):
        save_button = self.find_element(By.ID, "save_button")
        save_button.click()

    def is_password_recovery_successful(self):
        success_message = self.find_element(By.XPATH, "//*[contains(text(), 'Пароль успешно изменен')]")
        return success_message.is_displayed()

    def click_phone_radio(self):
        phone_radio = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(AuthPageLocators.PHONE_RADIO)
        )
        phone_radio.click()

