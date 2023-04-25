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
        #self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла"""
        with open('/home/dasha/electronics-shop-project/src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row["name"], row["price"], row["quantity"]))
        return len(cls.all)


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
        self.__name = name
        if len(name) <= 10:
            print("Длина наименования товара меньше 10 символов")
        else:
            print("Длина наименования товара превышает 10 символов.")

