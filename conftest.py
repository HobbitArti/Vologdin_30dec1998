import pytest
import allure
from selenium import webdriver
from user_api import Api



@allure.title("Фикстура URL для API-тестов")
@pytest.fixture(scope="session")
def api():
    return Api("https://www.sibdar-spb.ru")


@allure.title("Фикстура для браузера для UI-тестов")
@pytest.fixture
def driver():
    with allure.step("Записать в переменную browser, браузер 'Chrome'"):
        browser = webdriver.Chrome()

    with allure.step("Задать размеры окна браузера"):
        browser.maximize_window()

    yield browser  # Предоставьте браузер для использования в тестах

    with allure.step("Закрыть браузер"):
        browser.quit()