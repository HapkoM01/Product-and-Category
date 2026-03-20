import pytest
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.base_product import BaseProduct
from src.mixins import ReprMixin
from src.iterators import CategoryIterator

def test_repr_mixin_initialization(capsys):
    """Тест вывода информации при создании объекта"""
    product = Product("Test Product", "Test Description", 100.0, 10)

    captured = capsys.readouterr()
    assert "Product('Test Product', 'Test Description', 100.0, 10)" in captured.out


def test_repr_method():
    """Тест метода __repr__"""
    product = Product("Test Product", "Test Description", 100.0, 10)

    repr_str = repr(product)
    assert "Product" in repr_str
    assert "name='Test Product'" in repr_str or "name=Test Product" in repr_str


def test_mixin_inheritance():
    """Тест, что Product наследует ReprMixin"""
    assert issubclass(Product, ReprMixin)

    product = Product("Test", "Desc", 100.0, 10)
    assert isinstance(product, ReprMixin)


def test_smartphone_with_mixin(capsys):
    """Тест работы миксина с Smartphone"""
    phone = Smartphone(
        "Phone", "Desc", 200.0, 5,
        "Fast", "Pro", "256GB", "Silver"
    )

    captured = capsys.readouterr()
    assert "Smartphone('Phone', 'Desc', 200.0, 5, 'Fast', 'Pro', '256GB', 'Silver')" in captured.out


def test_lawn_grass_with_mixin(capsys):
    """Тест работы миксина с LawnGrass"""
    grass = LawnGrass(
        "Grass", "Desc", 50.0, 100,
        "Russia", "10 days", "Green"
    )

    captured = capsys.readouterr()
    assert "LawnGrass('Grass', 'Desc', 50.0, 100, 'Russia', '10 days', 'Green')" in captured.out
