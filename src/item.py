import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """Возвращает название класса, имя, цену и колическтво в виде строки"""
        return f"{self.__class__.__name__}" \
               f"('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает имя товара"""
        return f"{self.__name}"


    def __add__(self, other):
        """Функция сложения экземпляров класса"""
        if isinstance(other, Item):
            return self.quantity + other.quantity


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item данными из файла"""
        cls.all = []
        with open('../src/items.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row["name"], row["price"], row["quantity"]))


    @staticmethod
    def string_to_number(number: str):
        """Статический метод возвращающий число из строки"""
        return int(float(number))


    @property
    def name(self):
        """Возвращает имя"""
        return self.__name


    @name.setter
    def name(self, name):
        """Проверяет, что длина наименования товара не больше 10 символов"""
        if len(name) <= 10:
            self.__name = name
        else:
            print("""
Exception: Длина наименования товара превышает 10 символов.
            """)
