from src.item import Item

class MixinKeyboard:

    language = "EN"
    def __init__(self):
        self.language = language

    def __str__(self):
        return f"{self.language}"

    def change_lang(self):
        """Метод переключающий язык на клавиатуре между "EN" и "RU"""
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Item, MixinKeyboard):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)




