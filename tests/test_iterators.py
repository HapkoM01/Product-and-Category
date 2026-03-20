import pytest
from src.category import Category
from src.product import Product
from src.iterators import CategoryIterator


@pytest.fixture
def sample_category():
    """Фикстура для создания тестовой категории"""
    products = [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 10),
        Product("Product 3", "Description 3", 300.0, 15)
    ]
    return Category("Test Category", "Test Description", products)


def test_category_iterator(sample_category):
    """Тест итератора категории"""
    iterator = CategoryIterator(sample_category)
    products = list(iterator)

    assert len(products) == 3
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2"
    assert products[2].name == "Product 3"


def test_category_iterator_in_for_loop(sample_category):
    """Тест использования итератора в цикле for"""
    iterator = CategoryIterator(sample_category)
    names = []

    for product in iterator:
        names.append(product.name)

    assert names == ["Product 1", "Product 2", "Product 3"]


def test_category_iterator_empty():
    """Тест итератора для пустой категории"""
    empty_category = Category("Empty", "Description", [])
    iterator = CategoryIterator(empty_category)

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_exhaustion(sample_category):
    """Тест истощения итератора"""
    iterator = CategoryIterator(sample_category)

    # Проходим все элементы
    list(iterator)

    # Пытаемся получить следующий элемент
    with pytest.raises(StopIteration):
        next(iterator)
