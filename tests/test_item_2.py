from src.item import Item
import pytest

item = Item('Ноутбук', 20000, 10)
item_2 = Item('Суперноутбук', 20000, 10)

def test_name():
    assert item.name == 'Ноутбук'
    item.name = 'Суперноутбук'
    assert item.name == 'Ноутбук'
    assert item_2.name == 'Суперноутбук'

def test_string_to_number():
     assert item.string_to_number("10") == 10
     assert item.string_to_number("1.1") == 1
     assert item.string_to_number("-20") == -20



def test_repr():
    assert repr(item) == "Item('Ноутбук', 20000, 10)"
    assert repr(item_2) == "Item('Суперноутбук', 20000, 10)"


def test_str():
    assert str(item) == 'Ноутбук'
    assert str(item_2) == 'Суперноутбук'

def test_instantiate_from_csv():

    with pytest.raises(FileNotFoundError):
        try:
            with open('../src/item.csv', newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

def test_instantiate_from_csv_1():

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
