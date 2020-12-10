import unittest
from models.item import Item
from models.manufacturer import Manufacturer

class TestItem(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer("Gorbruz' Gutspillaz", "Simple and Brutal. From an Orc's forge to your mate's face!", "Melee weapons")
        self.item = Item("+1 Mace of Squishing", "A handy 1h weapon, enchanted for that extra *CRUNCH*", "Blunt 1h", 2, 5, self.manufacturer)

    def test_item_has_name(self):
        self.assertEqual("+1 Mace of Squishing" , self.item.name)

    def test_item_has_description(self):
        self.assertEqual("A handy 1h weapon, enchanted for that extra *CRUNCH*" , self.item.description)

    def test_item_has_category(self):
        self.assertEqual("Blunt 1h" , self.item.category)

    def test_item_has_buy_cost(self):
        self.assertEqual(2 , self.item.buy_cost)

    def test_item_has_sell_price(self):
        self.assertEqual(5 , self.item.sell_price)

    def test_item_has_manufacturer(self):
        self.assertEqual("Gorbruz' Gutspillaz" , self.item.manufacturer.name)

    def test_item_has_low_stock(self):
        self.item.stock = 1
        self.assertEqual(True , self.item.check_has_low_stock())

    def test_item_has_not_got_low_stock(self):
        self.item.stock = 6
        self.assertEqual(False , self.item.check_has_low_stock())

    def test_item_has_sold_out(self):
        self.assertEqual(False , self.item.check_has_sold_out())

    def test_item_has_not_sold_out(self):
        self.item.stock = 1
        self.assertEqual(True, self.item.check_has_sold_out())