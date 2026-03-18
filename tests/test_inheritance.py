import pytest
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category


def test_product_addition_same_class():
    """Тест сложения продуктов одного класса"""
    phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.0, "Model1", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 2000.0, 3, 96.0, "Model2", 256, "White")

    expected_sum = 1000 * 2 + 2000 * 3  # 2000 + 6000 = 8000
    assert phone1 + phone2 == expected_sum


def test_product_addition_different_classes():
    """Тест сложения продуктов разных классов (должно вызывать ошибку)"""
    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "Model", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7 days", "Green")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        result = phone + grass


def test_category_add_product_with_type_check():
    """Тест добавления продукта в категорию с проверкой типа"""
    category = Category("Test", "Description")
    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "Model", 128, "Black")

    # Добавление правильного типа
    category.add_product(phone)
    assert len(category.products_list) == 1

    # Добавление неправильного типа
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        category.add_product("Not a product")

    with pytest.raises(TypeError):
        category.add_product(123)


def test_category_product_count_with_inheritance():
    """Тест подсчета продуктов при использовании наследников"""
    Category.category_count = 0
    Category.product_count = 0

    phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 95.0, "Model1", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 2000.0, 3, 96.0, "Model2", 256, "White")
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7 days", "Green")

    category = Category("Test", "Description", [phone1, phone2])
    assert Category.product_count == 2

    category.add_product(grass)
    assert Category.product_count == 3


def test_new_product_classmethod_with_inheritance():
    """Тест класс-метода new_product с наследниками"""
    product_data = {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 1000.0,
        'quantity': 5
    }

    # Создание базового продукта
    product = Product.new_product(product_data)
    assert isinstance(product, Product)

    # Создание смартфона через обычный конструктор
    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "Model", 128, "Black")
    assert isinstance(phone, Smartphone)
    assert isinstance(phone, Product)
