from src.product import Product


class Category:
    """Класс для описания категории товаров"""

    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """Инициализация категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Увеличиваем счетчик категорий при создании объекта
        Category.category_count += 1

        # Увеличиваем счетчик товаров на длину списка продуктов
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Метод для добавления продукта в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов в отформатированном виде"""
        products_str = ""
        for product in self.__products:
            products_str += str(product) + "\n"
        return products_str

    @property
    def products_list(self):
        """Геттер для получения списка продуктов (для тестов)"""
        return self.__products

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
