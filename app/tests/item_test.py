import unittest
from models.item import Item

class TestItem(unittest.TestCase):
    
    def setUp(self):
        self.item = Item("+1 Mace of Squishing", "A handy 1h weapon, enchanted for that extra *CRUNCH*", "Blunt 1h", 2, 5, "Gorbruz' Gutspillaz")

    def test_item_has_name(self):
        pass

    def test_item_has_description(self):
        pass

    def test_item_has_category(self):
        pass

    def test_item_has_buy_cost(self):
        pass

    def test_item_has_sell_price(self):
        pass

    def test_item_has_manufacturer(self):
        pass