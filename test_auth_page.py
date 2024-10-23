import os
import time
import pytest
from pages.auth_page import AuthPage
from dotenv import load_dotenv
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import AuthPageLocators

# Загружаем переменные окружения из файла .env
load_dotenv()

# 1
@pytest.mark.usefixtures("selenium")
def test_auth_with_valid_credentials(selenium):
    """Проверка успешной авторизации с корректными учетными данными логин и пароль."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    login = os.getenv('VALID_LOGIN')
    password = os.getenv('VALID_PASSWORD')
    page.enter_email_or_phone(login)
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    # Ожидаем переход на страницу личного кабинета
    try:
        WebDriverWait(selenium, 30).until(EC.url_contains("account_b2c"))
        assert "account_b2c" in selenium.current_url, "Авторизация не выполнена, пользователь не перенаправлен в личный кабинет"
    except TimeoutException:
        assert False, "Не удалось дождаться перехода на страницу личного кабинета после авторизации"

    # Добавьте дополнительную проверку на наличие элемента, характерного для личного кабинета
    try:
        element = WebDriverWait(selenium, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-header-menu__link-text")))
        assert element.is_displayed(), "Элемент личного кабинета не отображается, авторизация могла не выполниться"
    except TimeoutException:
        assert False, "Не удалось дождаться отображения элемента личного кабинета"


# 2
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_login(selenium):
    """Проверка авторизации с неверным логином."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    page.enter_email_or_phone("invalid_user")
    password = os.getenv('VALID_PASSWORD')
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 3
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_password(selenium):
    """Проверка авторизации с неверным паролем."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    login = os.getenv('VALID_LOGIN')
    page.enter_email_or_phone(login)
    page.enter_password("invalid_password")

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 4
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_login_and_password(selenium):
    """Проверка авторизации с неверным логином и неверным паролем."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    page.enter_email_or_phone("invalid_user")
    page.enter_password("invalid_password")

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 5
@pytest.mark.usefixtures("selenium")
def test_auth_with_valid_email_and_password(selenium):
    """Проверка авторизации с корректной почтой и корректным паролем."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    email = os.getenv('VALID_EMAIL')
    password = os.getenv('VALID_PASSWORD')

    page.enter_email_or_phone(email)
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    assert "account_b2c" in page.get_current_url(), "Авторизация не выполнена, пользователь не перенаправлен в личный кабинет"


# 6
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_email(selenium):
    """Проверка авторизации с неверной почтой."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    page.enter_email_or_phone('invalid_email@example.com')
    password = os.getenv('VALID_PASSWORD')
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 7
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_email(selenium):
    """Проверка авторизации с верной почтой и неверным паролем."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    email = os.getenv('VALID_EMAIL')
    page.enter_email_or_phone(email)
    page.enter_password("invalid_password")

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 8
@pytest.mark.usefixtures("selenium")
def test_auth_with_valid_phone_and_password(selenium):
    """Проверка успешной авторизации по номеру телефона и паролю."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    phone = os.getenv('VALID_PHONE')
    password = os.getenv('VALID_PASSWORD')

    page.enter_email_or_phone(phone)
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    assert "account_b2c" in page.get_current_url(), "Авторизация не выполнена, пользователь не перенаправлен в личный кабинет"


# 9
@pytest.mark.usefixtures("selenium")
def test_auth_with_invalid_phone(selenium):
    """Проверка авторизации по номеру телефона с некорректным номером."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    page.enter_email_or_phone("+790000000")
    password = os.getenv('VALID_PASSWORD')
    page.enter_password(password)

    time.sleep(30)

    page.click_login_button()

    # Проверка сообщения "Неверный формат телефона" вместо двойной проверки
    assert "Неверный формат телефона" in page.get_error_message(), "Ожидаемая подсказка не отображается"


# 10
@pytest.mark.usefixtures("selenium")
def test_auth_with_valid_phone_and_invalid_password(selenium):
    """Проверка авторизации по номеру телефона с неверным паролем."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    phone = os.getenv('VALID_PHONE')
    page.enter_email_or_phone(phone)
    page.enter_password("invalid_password")

    time.sleep(30)

    page.click_login_button()

    assert page.get_error_message() == "Неверный логин или пароль", "Ожидаемая ошибка не отображается"


# 11-17

@pytest.mark.parametrize("password, confirm_password, expected_error", [
    ("abcde", "abcde", "Длина пароля должна быть не менее 8 символов"),
    ("Abcde198219821982198219821982198219821982", "Abcde198219821982198219821982198219821982", "Длина пароля должна быть не более 20 символов"),
    ("Abcdefgh", "Abcdefgh", "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"),
    ("nouppercase1", "nouppercase1", "Пароль должен содержать хотя бы одну заглавную букву"),
    ("NOLOWERCASE1", "NOLOWERCASE1", "Пароль должен содержать хотя бы одну строчную букву"),
    ("Абвдг1234", "Абвдг1234", "Пароль должен содержать только латинские буквы"),
    ("Valid_password1", "Different_password1", "Пароли не совпадают"),
])
@pytest.mark.usefixtures("selenium")
def test_password_validation_via_auth_page(selenium, password, confirm_password, expected_error):
    """Параметризованный тест для проверки правильности ввода пароля через страницу авторизации."""

    # Переход на страницу авторизации
    auth_page = AuthPage(selenium)
    auth_page.open("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=447cea39-c497-4333-9ec0-8031a11dbab7&theme=light")

    # Переход на страницу регистрации
    auth_page.click_register_link()

    # Ожидание загрузки страницы регистрации
    registration_page = RegistrationPage(selenium)

    # Вводим корректные данные для регистрации
    registration_page.enter_first_name("Регина")
    registration_page.enter_last_name("Спащенко")
    registration_page.enter_email("znaika@bk.ru")

    # Вводим пароли
    registration_page.enter_password(password)
    registration_page.confirm_password(confirm_password)

    # Нажимаем кнопку регистрации
    registration_page.click_register_button()

    # Ожидание и проверка сообщения об ошибке
    error_message = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'rt-input-container__meta--error')]"))
    )

    # Проверяем, что сообщение об ошибке отображается
    actual_error = error_message.text

    # Проверяем, соответствует ли ошибка ожидаемой
    assert expected_error == actual_error, f"Ожидалось сообщение: '{expected_error}', но отображается: '{actual_error}'"

# 18
@pytest.mark.usefixtures("selenium")
def test_auth_with_temporary_code(selenium):
    """Проверка авторизации с использованием  кода."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%223F1C3F42-3A98-4F98-8317-0DF72CDFBB99%22%7D")

    # Вводим номер телефона
    page.enter_phone_number(os.getenv('VALID_PHONE'))

    time.sleep(20)

    # Нажимаем кнопку "Получить код"
    page.click_get_code_button()

    # Проверяем, что отображена форма для ввода  кода
    assert page.is_code_input_form_displayed(), "Форма для ввода кода не отображена"

    # Вводим временный код вручную
    temp_code = input("Введите код, полученный на телефон: ")
    page.enter_temporary_code(temp_code)

    time.sleep(20)

    # Проверяем успешную авторизацию и редирект в личный кабинет
    assert "account_b2c" in page.get_current_url(), "Авторизация не выполнена, пользователь не перенаправлен в личный кабинет"

# 19
@pytest.mark.usefixtures("selenium")
def test_auth_with_blocked_cookies_no_popup(selenium):
    """Проверка авторизации с отключенными файлами cookie и отсутствием pop-up сообщения."""
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    # Блокируем cookie через настройки браузера
    selenium.delete_all_cookies()

    # Вводим корректные данные для авторизации
    login = os.getenv('VALID_LOGIN')
    password = os.getenv('VALID_PASSWORD')

    page.enter_email_or_phone(login)
    page.enter_password(password)

    # Нажимаем кнопку входа
    page.click_login_button()

    # Проверяем, что pop-up о необходимости включения cookie не появляется
    try:
        WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Cookie отключены')]"))
        )
        # Если pop-up появляется, тест проваливается, так как его быть не должно
        assert False, "Сообщение о необходимости включения cookie отображается, но не должно"
    except TimeoutException:
        # Если pop-up не появился, это ожидаемое поведение
        assert True, "Сообщение о необходимости включения cookie отсутствует"

    # Ожидаем завершения загрузки страницы (можно использовать любой элемент, характерный для личного кабинета)
    try:
        WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Личный кабинет')]"))
        )
        # Если личный кабинет загружается, проверим наличие cookie
        cookies = selenium.get_cookies()
        if not cookies:
            assert False, "Авторизация не должна была быть успешной, поскольку cookie отключены"
        else:
            assert True, "Авторизация выполнена, cookie были включены после входа"
    except TimeoutException:
        # Если личный кабинет не загружается, это ожидаемое поведение
        assert True, "Авторизация не выполнена, поскольку cookie отключены"

# 20
@pytest.mark.usefixtures("selenium")
def test_switching_to_login_tab(selenium):
    # Переход на страницу авторизации
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    # Ожидание появления вкладки "Телефон"
    phone_tab = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone"))
    )
    assert phone_tab.is_displayed(), "Вкладка 'Телефон' не отображается"

    # Переключение на вкладку "Логин"
    login_tab = selenium.find_element(By.ID, "t-btn-tab-login")
    login_tab.click()

    # Ожидание появления поля для ввода логина
    login_input = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    assert login_input.is_displayed(), "Поле для ввода логина не отображается"


#21
@pytest.mark.usefixtures("selenium")
def test_password_recovery_by_phone(selenium):
    page = AuthPage(selenium)
    selenium.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    # Переход на страницу восстановления пароля
    forgot_password_link = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))
    )
    forgot_password_link.click()

    # Нажатие на вкладку "Телефон"
    phone_tab = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "t-btn-tab-phone"))
    )
    phone_tab.click()

    # Ожидание появления поля для ввода номера телефона
    phone_input = WebDriverWait(selenium, 15).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    assert phone_input.is_displayed(), "Поле для ввода номера телефона не отображается"

    # Ввод номера телефона
    phone_number = os.getenv('VALID_PHONE')
    phone_input.clear()
    phone_input.send_keys(phone_number)

    # Добавление задержки
    import time
    time.sleep(20)

    # Нажатие кнопки "Продолжить"
    submit_button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "reset"))
    )
    submit_button.click()

    # Нажатие кнопки "По номеру телефона"
    phone_radio = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='rt-radio__circle']"))
    )
    phone_radio.click()

    # Нажатие кнопки "Продолжить"
    submit_button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "reset-form-submit"))
    )
    submit_button.click()

    # Ожидание загрузки формы для ввода SMS-кода
    sms_confirmation_message = WebDriverWait(selenium, 15).until(
        EC.presence_of_element_located((By.ID, "otp-code-form-description"))
    )
    assert sms_confirmation_message.is_displayed(), "Сообщение о коде подтверждения не отображается"
    sms_code_form = WebDriverWait(selenium, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Введите код из SMS')]"))
    )
    assert sms_code_form.is_displayed(), "Форма для ввода SMS-кода не отображается"

    # Ввод кода из SMS
    temp_code = input("Введите код из SMS: ")
    sms_input = selenium.find_element(By.ID, "rt-code-input")
    sms_input.clear()
    sms_input.send_keys(temp_code)

    # Ожидание формы для ввода нового пароля
    new_password_form = WebDriverWait(selenium, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Новый пароль')]"))
    )
    assert new_password_form.is_displayed(), "Форма для ввода нового пароля не отображается"

    # Ввод нового пароля из переменной окружения
    new_password = os.getenv('NEW_PASSWORD')
    assert new_password is not None, "Переменная NEW_PASSWORD не установлена"
    new_password_input = selenium.find_element(By.ID, "password-new")
    confirm_password_input = selenium.find_element(By.ID, "password-confirm")
    new_password_input.send_keys(new_password)
    confirm_password_input.send_keys(new_password)

    # Нажатие кнопки "Сохранить"
    save_button = WebDriverWait(selenium, 30).until(
        EC.element_to_be_clickable((By.ID, "t-btn-reset-pass"))
    )
    save_button.click()

    # Ожидание перехода на страницу авторизации
    selenium.get(
        "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=25bc7fe4-95e1-4a3f-b437-6e7a4e8cb782")

    # Ожидание появления поля для ввода номера телефона
    phone_input = WebDriverWait(selenium, 15).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    assert phone_input.is_displayed(), "Поле для ввода номера телефона не отображается"

    # Ввод номера телефона
    phone_input.clear()
    phone_input.send_keys(phone_number)

    # Ожидание появления поля для ввода пароля
    password_input = WebDriverWait(selenium, 15).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    assert password_input.is_displayed(), "Поле для ввода пароля не отображается"

    # Ввод пароля из переменной окружения
    password_input.send_keys(new_password)

    # Нажатие кнопки "Войти"
    login_button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    # Проверка успешной авторизации
    assert page.is_password_recovery_successful(), "Пароль не был успешно изменен"