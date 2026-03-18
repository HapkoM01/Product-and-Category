import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category(
        "Смартфоны",
        ("Смартфоны, как средство не только коммуникации, "
         "но и получения дополнительных функций для удобства жизни"),
        sample_products
    )


def test_category_initialization(sample_category, sample_products):
    """Тест корректности инициализации категории"""
    assert sample_category.name == "Смартфоны"
    expected_description = (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert sample_category.description == expected_description
    assert sample_category.products_list == sample_products


def test_products_private_attribute():
    """Тест приватности атрибута products"""
    category = Category("Test", "Description", [])

    with pytest.raises(AttributeError):
        category.__products

    assert category.products_list == []


def test_add_product():
    """Тест метода добавления продукта"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Test Category", "Test Description")
    assert category.products_list == []

    product = Product("Test Product", "Test Description", 100.0, 5)
    category.add_product(product)

    assert len(category.products_list) == 1
    assert category.products_list[0] == product
    assert Category.product_count == 1


def test_products_getter_format(sample_category):
    """Тест формата вывода геттера products"""
    products_str = sample_category.products

    # Проверяем, что используется __str__ продукта
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products_str

    assert products_str.count('\n') == 3


def test_add_product_increases_product_count():
    """Тест увеличения счетчика продуктов при добавлении"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Test", "Description")
    assert Category.product_count == 0

    product1 = Product("Product 1", "Description", 100.0, 1)
    product2 = Product("Product 2", "Description", 200.0, 2)

    category.add_product(product1)
    assert Category.product_count == 1

    category.add_product(product2)
    assert Category.product_count == 2


def test_category_count():
    """Тест подсчета количества категорий"""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Product 1", "Description 1", 100.0, 1)

    Category("Category 1", "Description 1", [product1])
    assert Category.category_count == 1

    Category("Category 2", "Description 2", [product1])
    assert Category.category_count == 2


def test_category_str_method(sample_category, sample_products):
    """Тест строкового представления категории"""
    total_quantity = sum(p.quantity for p in sample_products)
    expected_str = f"Смартфоны, количество продуктов: {total_quantity} шт."
    assert str(sample_category) == expected_str
