import pytest
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Description", 100.0, 0)


def test_product_negative_quantity():
    """Тест создания продукта с отрицательным количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Description", 100.0, -5)


def test_smartphone_zero_quantity():
    """Тест создания смартфона с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Smartphone("Phone", "Desc", 1000.0, 0, "Fast", "Pro", "128GB", "Black")


def test_lawn_grass_zero_quantity():
    """Тест создания газонной травы с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        LawnGrass("Grass", "Desc", 500.0, 0, "Russia", "7 days", "Green")


def test_category_middle_price_normal():
    """Тест подсчета среднего ценника в категории с товарами"""
    product1 = Product("P1", "Desc", 100.0, 10)
    product2 = Product("P2", "Desc", 200.0, 5)
    product3 = Product("P3", "Desc", 300.0, 2)

    category = Category("Test", "Description", [product1, product2, product3])

    expected_middle = (100.0 + 200.0 + 300.0) / 3
    assert category.middle_price() == expected_middle


def test_category_middle_price_empty():
    """Тест подсчета среднего ценника в пустой категории"""
    category = Category("Empty", "Description", [])

    assert category.middle_price() == 0


def test_category_middle_price_single_product():
    """Тест подсчета среднего ценника в категории с одним товаром"""
    product = Product("P1", "Desc", 150.0, 10)
    category = Category("Test", "Description", [product])

    assert category.middle_price() == 150.0


def test_category_middle_price_with_smartphone():
    """Тест подсчета среднего ценника с разными типами продуктов"""
    product = Product("P1", "Desc", 100.0, 10)
    phone = Smartphone("Phone", "Desc", 200.0, 5, "Fast", "Pro", "128GB", "Black")

    category = Category("Test", "Description", [product, phone])

    expected_middle = (100.0 + 200.0) / 2
    assert category.middle_price() == expected_middle


def test_new_product_with_zero_quantity():
    """Тест создания продукта через new_product с нулевым количеством"""
    product_data = {
        'name': 'Test',
        'description': 'Desc',
        'price': 100.0,
        'quantity': 0
    }

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product.new_product(product_data)
