from src.product import Product
from src.category import Category
from src.iterators import CategoryIterator  # для дополнительного задания


if __name__ == '__main__':
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Тестирование __str__ для Product
    print("=== Тестирование __str__ для Product ===")
    print(str(product1))
    print(str(product2))
    print(str(product3))

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Тестирование __str__ для Category
    print("\n=== Тестирование __str__ для Category ===")
    print(str(category1))

    # Тестирование геттера products
    print("\n=== Тестирование геттера products ===")
    print(category1.products)

    # Тестирование __add__ для Product
    print("\n=== Тестирование __add__ для Product ===")
    print(f"{product1.name} + {product2.name} = {product1 + product2}")
    print(f"{product1.name} + {product3.name} = {product1 + product3}")
    print(f"{product2.name} + {product3.name} = {product2 + product3}")

    # Дополнительно: проверка итератора (из предыдущего задания)
    print("\n=== Тестирование итератора CategoryIterator (доп. задание) ===")
    iterator = CategoryIterator(category1)
    for i, product in enumerate(iterator, 1):
        print(f"Товар {i}: {product}")
