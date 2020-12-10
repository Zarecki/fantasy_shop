import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer("Gorbruz' Gutspillaz", "Simple and Brutal. From an Orc's forge to your mate's face!", "Melee weapons")

    def test_manufacturer_has_name(self):
        pass

    def test_manufacturer_has_description(self):
        pass

    def test_manufacturer_has_category(self):
        pass