import pytest
from src.base_product import BaseProduct
from src.product import Product


def test_base_product_abstract():
    """Тест, что BaseProduct является абстрактным классом"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100.0, 10)


def test_base_product_price_property():
    """Тест property price в BaseProduct через наследника"""
    product = Product("Test", "Desc", 100.0, 10)

    # Тест геттера
    assert product.price == 100.0

    # Тест сеттера с положительным значением
    product.price = 150.0
    assert product.price == 150.0

    # Тест сеттера с нулевым значением (должно вывести сообщение)
    product.price = 0
    assert product.price == 150.0  # Не должно измениться


def test_base_product_abstract_methods():
    """Тест наличия абстрактных методов"""
    assert hasattr(BaseProduct, 'get_info')
    assert hasattr(BaseProduct, '__str__')
    assert hasattr(BaseProduct, '__add__')
    assert callable(BaseProduct.get_info)
