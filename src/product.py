class Product:
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
