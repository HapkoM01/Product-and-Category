from src.product import Product


class LawnGrass(Product):
    """Класс для газонной травы - наследник Product"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """Инициализация газонной травы"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление газонной травы"""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}")
