from src.category import Category


class CategoryIterator:
    """Итератор для перебора товаров в категории"""

    def __init__(self, category: Category):
        """Инициализация итератора"""
        self._category = category
        self._index = 0

    def __iter__(self):
        """Возвращает итератор"""
        return self

    def __next__(self):
        """Возвращает следующий товар"""
        products = self._category.products_list
        if self._index < len(products):
            product = products[self._index]
            self._index += 1
            return product
        raise StopIteration
