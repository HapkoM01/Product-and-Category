from src.product import Product


class Category:
    """Класс для описания категории товаров"""

    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий при создании объекта
        Category.category_count += 1

        # Увеличиваем счетчик товаров на длину списка продуктов
        Category.product_count += len(self.products)
