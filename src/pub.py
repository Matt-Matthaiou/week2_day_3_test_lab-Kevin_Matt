from src.customer import Customer

class Pub:
    
    def __init__(self, name, till,):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_stock(self, drink):
        self.drinks.append(drink)

    
    def customer_order(self, drink_name, customer):
        # print(drink_name)
        # print(customer)
        drink_price = 0
        for item in self.drinks:
            if item.name == drink_name:
                drink_price = item.price
        
        # print(drink_price)
        self.increase_till(drink_price)
        customer.reduce_wallet(drink_price)
