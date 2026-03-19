import pytest
from src.base_product import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_base_product_abstract():
    """Тест, что BaseProduct является абстрактным классом"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100.0, 10)


def test_product_inheritance():
    """Тест наследования Product от BaseProduct"""
    product = Product("Test", "Description", 100.0, 10)
    assert isinstance(product, BaseProduct)
    assert hasattr(product, 'get_info')
    assert hasattr(product, '__str__')
    assert hasattr(product, '__add__')


def test_smartphone_inheritance():
    """Тест наследования Smartphone"""
    phone = Smartphone(
        "Phone", "Desc", 1000.0, 10,
        "Fast", "Pro", "128GB", "Black"
    )
    assert isinstance(phone, Product)
    assert isinstance(phone, BaseProduct)
    assert hasattr(phone, 'get_info')
    assert callable(phone.get_info)


def test_lawn_grass_inheritance():
    """Тест наследования LawnGrass"""
    grass = LawnGrass(
        "Grass", "Desc", 500.0, 100,
        "Russia", "10 days", "Green"
    )
    assert isinstance(grass, Product)
    assert isinstance(grass, BaseProduct)
    assert hasattr(grass, 'get_info')
    assert callable(grass.get_info)


def test_get_info_methods():
    """Тест метода get_info для разных классов"""
    # Product
    product = Product("Product", "Desc", 100.0, 10)
    assert "Product - Desc" in product.get_info()

    # Smartphone
    phone = Smartphone(
        "Phone", "Smart Desc", 200.0, 5,
        "Fast", "Pro", "256GB", "Silver"
    )
    info = phone.get_info()
    assert "Смартфон: Phone Pro" in info
    assert "Fast, 256GB, Silver" in info

    # LawnGrass
    grass = LawnGrass(
        "Grass", "Grass Desc", 50.0, 100,
        "Russia", "10 days", "Green"
    )
    info = grass.get_info()
    assert "Газонная трава: Grass" in info
    assert "Russia, 10 days, Green" in info
