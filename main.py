from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

if __name__ == '__main__':
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("=" * 60)

    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
        print(f"Сообщение: {e}")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ СОЗДАНИЯ ОБЫЧНЫХ ПРОДУКТОВ")
    print("=" * 60)

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"Создано {Category.product_count} продуктов")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ МЕТОДА MIDDLE_PRICE")
    print("=" * 60)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(f"Средний ценник в категории '{category1.name}': {category1.middle_price()} руб.")

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средний ценник в пустой категории: {category_empty.middle_price()} руб.")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ НАСЛЕДНИКОВ С НУЛЕВЫМ КОЛИЧЕСТВОМ")
    print("=" * 60)

    try:
        smartphone_invalid = Smartphone("Phone", "Desc", 1000.0, 0, "Fast", "Pro", "128GB", "Black")
    except ValueError as e:
        print(f"Смартфон с нулевым количеством: {e}")

    try:
        grass_invalid = LawnGrass("Grass", "Desc", 500.0, 0, "Russia", "7 days", "Green")
    except ValueError as e:
        print(f"Газонная трава с нулевым количеством: {e}")
