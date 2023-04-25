"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item_1 = Item("Смартфон", 50000, 20)
item_2 = Item("Ноутбук", 20000, 0)
Item.pay_rate = 0.9
def test_item_total_price():
     assert item_1.calculate_total_price() == 1000000
     assert item_2.calculate_total_price() == 0

def test_item_apply_discount():
     Item.pay_rate = 0.9
     item_1.apply_discount()
     item_2.apply_discount()
     assert item_1.price == 45000
     assert item_2.price == 18000

