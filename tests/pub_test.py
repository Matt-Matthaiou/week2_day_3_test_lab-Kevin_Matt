import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink = Drinks("whisky", 5)
        self.drink2 = Drinks("vodka", 4)
        self.pub = Pub("The Prancing Pony", 100.000)
        self.customer = Customer("Matt", 30)
        self.pub.add_drink_to_stock(self.drink)
        self.pub.add_drink_to_stock(self.drink2)
        

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_drink_name(self):
        self.assertEqual("whisky", self.drink.name)
    
    def test_drink_price(self):
        self.assertEqual (5, self.drink.price)


    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_customer_order(self):
        self.pub.customer_order("vodka", self.customer)
        self.assertEqual (25, self.customer.wallet)
        self.assertEqual (105, self.pub.till)


