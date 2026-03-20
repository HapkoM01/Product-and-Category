from src.product import Product


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """Инициализация газонной травы"""
        # Проверка количества уже выполняется в родительском __init__
        super().__init__(name, description, price, quantity)

        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление газонной травы"""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Страна: {self.country}, Срок прорастания: {self.germination_period}, Цвет: {self.color}")

    def get_info(self) -> str:
        """Информация о газонной траве"""
        return (f"Газонная трава: {self.name}\n"
                f"Характеристики: {self.country}, {self.germination_period}, {self.color}\n"
                f"Цена: {self.price} руб., в наличии: {self.quantity} шт.")
