from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: str, color: str):
        """Инициализация смартфона"""
        # Сначала вызываем __init__ родителя
        super().__init__(name, description, price, quantity)

        # Затем добавляем специфичные атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона"""
        return (f"{self.name} ({self.model}), {self.price} руб. Остаток: {self.quantity} шт. "
                f"Характеристики: {self.efficiency}, {self.memory}, {self.color}")

    def get_info(self) -> str:
        """Информация о смартфоне"""
        return (f"Смартфон: {self.name} {self.model}\n"
                f"Характеристики: {self.efficiency}, {self.memory}, {self.color}\n"
                f"Цена: {self.price} руб., в наличии: {self.quantity} шт.")
