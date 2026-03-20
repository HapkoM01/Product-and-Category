from src.base_product import BaseProduct
from src.mixins import ReprMixin


class Product(ReprMixin, BaseProduct):
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта"""
        # Проверка на нулевое количество
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def get_info(self) -> str:
        """Реализация абстрактного метода"""
        return f"{self.name} - {self.description}, Цена: {self.price} руб., Количество: {self.quantity} шт."

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов по формуле цена * количество"""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)
