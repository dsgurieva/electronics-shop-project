from src.item import Item
from src.phone import Phone

item = Item('Ноутбук', 20000, 10)
item_2 = Item('Суперноутбук', 20000, 10)

phone = Phone('Смартфон', 15000, 5, 2)
phone_2 = Phone('Суперсмартфон', 150000, 1, 1)
phone_3 = Phone('Суперсмартфон', 150000, 1, 0)

def test_repr():

    assert repr(phone) == "Phone('Смартфон', 15000, 5, 2)"
    assert repr(phone_2) == "Phone('Суперсмартфон', 150000, 1, 1)"

def test_add():

    assert item + phone == 15
    assert phone_2 + phone == 6


def test_number_of_sim():

    assert phone.number_sim == 2
    assert phone_2.number_sim == 1
    assert phone_3.number_sim == 'ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.'

print(phone_3)