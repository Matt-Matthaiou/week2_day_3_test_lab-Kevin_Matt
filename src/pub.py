

class Pub:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []


    def find_drink_by_name(self, drink_name):

        if drink_name in self.drinks.keys():
            pass

    def increase_till(self, amount):
        self.till += amount