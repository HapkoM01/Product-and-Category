import pytest
from src.lawn_grass import LawnGrass


def test_lawn_grass_initialization():
    """Тест инициализации газонной травы"""
    grass = LawnGrass(
        "Test Grass", "Test Description", 500.0, 20,
        "Russia", "7 days", "Green"
    )

    assert grass.name == "Test Grass"
    assert grass.description == "Test Description"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"


def test_lawn_grass_str():
    """Тест строкового представления газонной травы"""
    grass = LawnGrass(
        "Test Grass", "Test Description", 500.0, 20,
        "Russia", "7 days", "Green"
    )

    expected_str = ("Test Grass, 500.0 руб. Остаток: 20 шт. "
                    "Страна: Russia, Срок прорастания: 7 days, Цвет: Green")
    assert str(grass) == expected_str


def test_lawn_grass_inheritance():
    """Тест наследования от Product"""
    grass = LawnGrass(
        "Test Grass", "Test Description", 500.0, 20,
        "Russia", "7 days", "Green"
    )

    # Проверяем, что атрибуты Product доступны
    assert hasattr(grass, 'name')
    assert hasattr(grass, 'description')
    assert hasattr(grass, 'price')
    assert hasattr(grass, 'quantity')

    # Проверяем, что методы Product работают
    grass.price = 550.0
    assert grass.price == 550.0
