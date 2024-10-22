from equipment import Equipment
## im importing the orignal class that is too be inherited from "Equipment" and have given the file name/location as "equipment"

class Heavy_Equipment(Equipment):
    def __init__(self):
        pass
    ##this is method overloading ona  constructor which is being overloaded by another constructor 
    
        ## we are creating a new ckass which inherites from the parent class "Equipment"
    def __init__(self, name, type, brand, description, fuel_type, renting_status=None):
        super().__init__(name, "Heavy", brand, description)
        ##the super function allows us to gain temp access of the the parent class which in this case would be the "Equipment" class it is method 
        ##overriding and it reduces code duplication 
        self.description = description
        self.fuel_type = fuel_type
        self.renting_status = renting_status  ## over here im using a data dictionary to hold renting status details, a data dictionary is a 
                                              ##data data strucutre similiar to that of a list 
    def PrintDetails(self, name, type, brand, description, fuel_type):
        super().PrintDetails(name, type, brand, description)
        print("Fuel type:", self.fuelt_type)

    def allocate(self, name, address, phone_number, start_of_rent, end_of_rent):
        self.renting_status = {
            "Name": name,
            "Address": address,
            "Phone number": phone_number,
            "Start of Rent": start_of_rent,
            "End of Rent": end_of_rent
        }

    def unallocate(self):
        self.renting_status = None