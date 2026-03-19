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
    # Создаем продукт и очищаем вывод от миксина
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Очищаем вывод от миксина
    capsys.readouterr()

    assert product.price == 100.0

    product.price = 150.0
    assert product.price == 150.0

    product.price = 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 150.0

    product.price = -50
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 150.0


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


def test_product_str_method():
    """Тест строкового представления продукта"""
    product = Product("Test Product", "Test Description", 100.0, 15)
    expected_str = "Test Product, 100.0 руб. Остаток: 15 шт."
    assert str(product) == expected_str


def test_product_add_method():
    """Тест сложения продуктов"""
    product1 = Product("Product 1", "Description", 100.0, 10)
    product2 = Product("Product 2", "Description", 200.0, 2)

    expected_sum = 100 * 10 + 200 * 2  # 1000 + 400 = 1400
    assert product1 + product2 == expected_sum

    # Проверка с разными значениями
    product3 = Product("Product 3", "Description", 50.0, 5)
    product4 = Product("Product 4", "Description", 300.0, 1)

    expected_sum = 50 * 5 + 300 * 1  # 250 + 300 = 550
    assert product3 + product4 == expected_sum


def test_product_add_with_non_product():
    """Тест сложения продукта с не-продуктом"""
    product = Product("Product", "Description", 100.0, 10)

    with pytest.raises(TypeError):
        result = product + 100


def test_product_add_different_classes():
    """Тест сложения продуктов разных классов"""
    from src.smartphone import Smartphone

    product = Product("Product", "Description", 100.0, 10)
    phone = Smartphone("Phone", "Desc", 200.0, 5, "Fast", "Pro", "128GB", "Black")

    with pytest.raises(TypeError, match="Нельзя складывать продукты разных классов"):
        result = product + phone
