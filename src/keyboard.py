from src.item import Item

class MixinKeyboard:

    __language = "EN"
    def __init__(self):
        self.__language = __language

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return f'{self.__language}'


    def change_lang(self):
        """Метод переключающий язык на клавиатуре между "EN" и "RU"""
        if self.__language == "EN":
            self.__language = "RU"
            return self
        elif self.__language == "RU":
            self.__language = "EN"
            return self
        else:
            raise AttributeError(": property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Item, MixinKeyboard):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)



