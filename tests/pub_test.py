import unittest
from src.pub import Pub
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("whisky" , 5)
        self.pub = Pub("The Prancing Pony", 100.000, self.drinks)
        

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_drink_name(self):
        self.assertEqual("whisky", self.drinks.name)
    
    def test_drink_price(self):
        self.assertEqual (5, self.drinks.price)

    # def test_find_drink_by_name(self):
    #    drink_from_drinks = find_drink_by_name("beer")
    #    self.assertEqual("vodka", drink_from_drinks)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

