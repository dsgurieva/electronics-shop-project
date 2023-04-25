from src.item import Item

item = Item('Ноутбук', 20000, 10)
item_2 = Item('Суперноутбук', 20000, 10)
def test_name():
    assert item.name == 'Ноутбук'
    assert item_2.name == "Суперноутбук"

def test_instantiate_from_csv():
    assert Item.instantiate_from_csv() == 5

def test_string_to_number():
     assert item.string_to_number("10") == 10
     assert item.string_to_number("1.1") == 1
     assert item.string_to_number("-20") == -20