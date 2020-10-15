import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Обработчик опции в функции для запуска с помощью параметра language нужен для запуска теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language please")

# Фикстура для открытия браузера с указанным языком
@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    options = Options()
    # Запуск браузера с указанным языком пользователя
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
