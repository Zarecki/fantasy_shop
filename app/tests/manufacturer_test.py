import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer("Gorbruz' Gutspillaz", "Simple and Brutal. From an Orc's forge to your mate's face!", "Melee weapons")

    def test_manufacturer_has_name(self):
        self.assertEqual("Gorbruz' Gutspillaz", self.manufacturer.name)

    def test_manufacturer_has_description(self):
        self.assertEqual("Simple and Brutal. From an Orc's forge to your mate's face!", self.manufacturer.description)

    def test_manufacturer_has_category(self):
        self.assertEqual("Melee weapons", self.manufacturer.category)

    def test_manufacturer_is_active(self):
        self.assertEqual(True, self.manufacturer.active)

    def test_manufacturer_is_not_active(self):
        self.manufacturer.make_inactive()
        self.assertEqual(False, self.manufacturer.active)

    def test_manufacturer_reactivate(self):
        self.manufacturer.make_inactive()
        self.assertEqual(False, self.manufacturer.active)
        self.manufacturer.reactivate()
        self.assertEqual(True, self.manufacturer.active)