import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов"""
    return [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        sample_products,
    )


def test_category_initialization(sample_category, sample_products):
    """Тест корректности инициализации категории"""
    assert sample_category.name == "Смартфоны"
    expected_description = (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert sample_category.description == expected_description
    assert sample_category.products == sample_products


def test_category_count():
    """Тест подсчета количества категорий"""
    # Сброс счетчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Product 1", "Description 1", 100.0, 1)

    Category("Category 1", "Description 1", [product1])
    assert Category.category_count == 1

    Category("Category 2", "Description 2", [product1])
    assert Category.category_count == 2


def test_product_count():
    """Тест подсчета количества продуктов"""
    # Сброс счетчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Product 1", "Description 1", 100.0, 1)
    product2 = Product("Product 2", "Description 2", 200.0, 2)
    product3 = Product("Product 3", "Description 3", 300.0, 3)

    Category("Category 1", "Description 1", [product1, product2])
    assert Category.product_count == 2

    Category("Category 2", "Description 2", [product1, product2, product3])
    assert Category.product_count == 5  # 2 + 3 = 5
