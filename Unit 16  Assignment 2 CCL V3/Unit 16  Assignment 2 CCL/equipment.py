class Equipment:
    def __init__(self, name, type, brand, description):
        self.name = name
        self.type = type
        self.brand = brand
        self.description = description
    
    def PrintDetails(self, name, type, brand, description):
        print("Product Name:", self.name)
        print("Brand:", self.type)
        print("Equipment Type:", self.brand)
        print("Description:", self.description)