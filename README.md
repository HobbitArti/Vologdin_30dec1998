# Vologdin_30dec98

## Тестирование интернет-магазина "Дикий сбор"

## ШАГИ
1. Склонировать проект 

2. Установить зависимости

4. Запустить тесты с указанием пути к директории результатов тестирования pytest pytest --alluredir allure-result

5. Сформировать отчет allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- allure

### Структура 
- ./test - тесты 
  - test_api.py - Api тесты
  - test_ui.py - Ui тесты
 - conftest.py - Файл с фикстурами 
 - user_api.py - Методы для Аpi тестов
 - main_page.py - Методы для UI тестов

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure
- pip install json

### Запуск тестов 
- pytest (Запуск всех тестов )
- python -m pytest --alluredir allure-result (Запустить тесты с указанием пути к каталогу результатов тестирования)
- allure serve allure-results (Запустить Allure и конвертирует результаты теста в отчет)
