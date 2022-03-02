from src.customer import Customer

class Pub:
    
    def __init__(self, name, till,):
        self.name = name
        self.till = till
        self.drinks = []
        self.customers_in_pub = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_stock(self, drink):
        self.drinks.append(drink)

    def check_customer_age (self, customer):
        if customer.age >= 18:
            # self.customers_in_pub.append(customer)
            return True
        else:
            return False

    def check_drunknness(self, customer):
        if customer.drunkenness < 6:
            return True
        else:
            return False

    
    def customer_order(self, drink_name, customer):
        drink_price = 0
        drink_level = 0
        if self.check_customer_age(customer) and self.check_drunknness(customer):
            for item in self.drinks:
                if item.name == drink_name:
                    drink_price = item.price
                    drink_level = item.alcohol_level

            customer.increase_drunkenness(drink_level)
            self.increase_till(drink_price)
            customer.reduce_wallet(drink_price)
