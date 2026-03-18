from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов - наследник Product"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """Инициализация смартфона"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона"""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Модель: {self.model}, Память: {self.memory}GB, Цвет: {self.color}")
