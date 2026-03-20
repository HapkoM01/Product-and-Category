from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация базового продукта"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @abstractmethod
    def get_info(self) -> str:
        """Абстрактный метод для получения информации о продукте"""
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения продуктов"""
        pass
