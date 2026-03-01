# Домашнее задание 14.1

## Описание проекта
Проект для работы с классами Product (Товар) и Category (Категория товаров).

## Реализованный функционал
- Класс Product с атрибутами: name, description, price, quantity
- Класс Category с атрибутами: name, description, products
- Атрибуты класса Category: category_count (количество категорий) и product_count (количество товаров)
- Автоматический подсчет количества категорий и товаров при создании объектов

## Тестирование

Проект использует `pytest` для тестирования.

### Запуск тестов

```bash
# Запуск всех тестов
poetry run pytest

# Запуск с детальным выводом
poetry run pytest -v

# Запуск конкретного модуля
poetry run pytest tests/test_masks_pytest.py -v

# Запуск с покрытием кода
poetry run pytest --cov=src --cov-report=html

## Установка:

1. Клонируйте репозиторий:

```

git@github.com:HapkoM01/Product-and-Category.git

```

2. Установите зависимости:

```

pip install -r requirements.txt
poetry init
poetry add requests

```

## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

## Код написал:

HapkoM - Beginner Python-developer