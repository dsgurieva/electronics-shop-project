from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализация класса Phone"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        self.__number_of_sim = number_of_sim
        if number_of_sim <= 0:
            raise ValueError ("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            print(number_of_sim)

