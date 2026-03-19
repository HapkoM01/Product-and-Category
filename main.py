from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

if __name__ == '__main__':
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ MIXIN (при создании объектов будет вывод)")
    print("=" * 60)

    # Создание обычных продуктов (должен сработать миксин)
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("\n" + "=" * 60)
    print("ВЫВОД ИНФОРМАЦИИ О ПРОДУКТАХ")
    print("=" * 60)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ КАТЕГОРИИ")
    print("=" * 60)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ НОВЫХ КЛАССОВ (Smartphone и LawnGrass)")
    print("=" * 60)

    # Создание смартфона (миксин тоже сработает)
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "Флагманский смартфон",
        180000.0,
        5,
        "Snapdragon 8 Gen 2",
        "S23 Ultra",
        "256GB",
        "Серый"
    )

    # Создание газонной травы (миксин тоже сработает)
    grass = LawnGrass(
        "Газонная трава 'Изумруд'",
        "Быстрорастущая газонная трава",
        2500.0,
        50,
        "Россия",
        "7-10 дней",
        "Изумрудный"
    )

    print("\nИнформация о смартфоне (get_info):")
    print(smartphone.get_info())

    print("\nИнформация о газонной траве (get_info):")
    print(grass.get_info())

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ МЕТОДА __repr__")
    print("=" * 60)

    print(repr(smartphone))
    print(repr(grass))
