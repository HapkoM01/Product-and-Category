class ReprMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        """Инициализация с выводом информации"""
        # Вызываем родительский __init__ ДО вывода информации
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, **kwargs):
        """Перехватываем создание подклассов для добавления логирования"""
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            # Формируем строку с параметрами
            params = []
            for arg in args:
                params.append(repr(arg))
            for key, value in kwargs.items():
                params.append(f"{key}={repr(value)}")

            params_str = ", ".join(params)
            print(f"{cls.__name__}({params_str})")

            # Вызываем оригинальный __init__
            original_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    def __repr__(self):
        """Представление объекта"""
        attributes = []
        for key, value in self.__dict__.items():
            if not key.startswith('_') and not key.startswith('__'):
                attributes.append(f"{key}={repr(value)}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"
