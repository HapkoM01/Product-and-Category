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


def test_product_initialization_with_different_values():
    """Тест инициализации с другими значениями"""
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8
