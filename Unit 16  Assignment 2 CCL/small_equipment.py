from equipment import Equipment
## im importing the orignal class that is too be inherited from "Equipment" and have given the file name/location as "equipment"

class Small_Equipment(Equipment):
    def __init__(self, name, type, brand, description, quantity, price):
        super().__init__(name, "Small", brand, description)
        ##the super function allows us to gain temp access of the the parent class which in this case would be the "Equipment" class it is method 
        ##overriding and it reduces code duplication 
        self.quantity = quantity
        self.price = price


    def update_quantity(self, quantity):
        self.quantity = quantity

    def update_price(self, price):
        self.price = price