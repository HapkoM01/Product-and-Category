import pytest
from src.smartphone import Smartphone


def test_smartphone_initialization():
    """Тест инициализации смартфона"""
    phone = Smartphone(
        "Test Phone", "Test Description", 50000.0, 10,
        95.5, "Test Model", 128, "Black"
    )

    assert phone.name == "Test Phone"
    assert phone.description == "Test Description"
    assert phone.price == 50000.0
    assert phone.quantity == 10
    assert phone.efficiency == 95.5
    assert phone.model == "Test Model"
    assert phone.memory == 128
    assert phone.color == "Black"


def test_smartphone_str():
    """Тест строкового представления смартфона"""
    phone = Smartphone(
        "Test Phone", "Test Description", 50000.0, 10,
        95.5, "Test Model", 128, "Black"
    )

    expected_str = ("Test Phone, 50000.0 руб. Остаток: 10 шт. "
                    "Модель: Test Model, Память: 128GB, Цвет: Black")
    assert str(phone) == expected_str


def test_smartphone_inheritance():
    """Тест наследования от Product"""
    phone = Smartphone(
        "Test Phone", "Test Description", 50000.0, 10,
        95.5, "Test Model", 128, "Black"
    )

    # Проверяем, что атрибуты Product доступны
    assert hasattr(phone, 'name')
    assert hasattr(phone, 'description')
    assert hasattr(phone, 'price')
    assert hasattr(phone, 'quantity')

    # Проверяем, что методы Product работают
    phone.price = 55000.0
    assert phone.price == 55000.0
