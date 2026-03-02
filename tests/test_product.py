import pytest
from src.product import Product


def test_product_initialization():
    """Тест корректности инициализации продукта"""
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_getter_setter(capsys):
    """Тест геттера и сеттера цены"""
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Проверка геттера
    assert product.price == 100.0

    # Проверка сеттера с положительным значением
    product.price = 150.0
    assert product.price == 150.0

    # Проверка сеттера с нулевым значением
    product.price = 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 150.0  # Цена не должна измениться

    # Проверка сеттера с отрицательным значением
    product.price = -50
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 150.0  # Цена не должна измениться


def test_new_product_classmethod():
    """Тест класс-метода new_product"""
    product_data = {
        'name': 'Iphone 15',
        'description': '512GB, Gray space',
        'price': 210000.0,
        'quantity': 8
    }

    product = Product.new_product(product_data)

    assert product.name == 'Iphone 15'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8
