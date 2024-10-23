from selenium.webdriver.common.by import By

class AuthPageLocators:
    PHONE_TAB = (By.ID, "t-btn-tab-phone")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    BTN_LOGIN = (By.ID, "kc-login")
    ERROR_MESSAGE = (By.XPATH, "//span[@id='form-error-message'] | //span[@id='username-meta']")
    REGISTER_LINK = (By.ID, "kc-register")
    PHONE_INPUT = (By.ID, "username")
    GET_CODE_BUTTON = (By.ID, "otp_get_code")
    CODE_INPUT_FORM = (By.ID, "rt-code-input")
    CODE_INPUT = (By.ID, "card-title")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")  # Новый локатор
    RESET_BUTTON = (By.ID, "reset")  # Новый локатор
    PASSWORD_RECOVERY_TITLE = (By.XPATH, "//*[contains(text(), 'Восстановление пароля')]")  # Новый локатор
    PHONE_RADIO = (By.XPATH, "//span[@class='rt-radio__label' and contains(text(), 'По номеру телефона')]")
class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    EMAIL_INPUT = (By.ID, 'address')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'password-confirm')
    REGISTER_BUTTON = (By.NAME, 'register')