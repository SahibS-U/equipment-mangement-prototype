from heavy_equipment import Heavy_Equipment
from small_equipment import Small_Equipment



def renting_details_getter():
    client_name = input("what is the client's name?\n")
    client_address = input("what is the client's address?\n")
    client_phone_no = input("what is the client's phone number?\n")
    start_date = input("what is the renting start date?\n")
    end_date = input("what is the end date?\n")
    
def heavyequipment_details_getter():
    temp_name = input("What is the name of the Equipment?\n")
    temp_brand = input("What is the Brand?\n")
    temp_description = input("Please provide a breif description of the product\n")
    temp_fuel = input("what is the fuel type\n")
    temp_renting_status = input("Is it being rented? If rented please enter yes, and if it is not then please enter N/a. Thank you!\n")
    temp_name = Heavy_Equipment(temp_name, "heavy", temp_brand, temp_description, temp_fuel, None)

instance_names = {}   ## i am creating another data dictionary to try and name my objects dynamically based on the name 
                       ## that the user have input for the equipment. this creates a dynamic naming system based on user inputs 





## im importing the both of the classes that i have create and from their respective programs
loop = True 
while loop == True:
    print("welcome to Construction Corporation's Equipment mangemnt software")
    answer_1 =  input("What would you like to do? \nIf regarding heavy equipment please enter 1 \nIf regarding small equipment please type 2\n")
    if answer_1 == "1":
        answer_2 = input("would you like to add a new heavy construction equipment\n") 
        if answer_2 == "yes":
            temp_name = input("What is the name of the Equipment?\n")
            temp_brand = input("What is the Brand?\n")
            temp_description = input("Please provide a breif description of the product\n")
            temp_fuel = input("what is the fuel type\n")
            temp_renting_status = input("Is it being rented? If rented please enter yes, and if it is not then please enter N/a. Thank you!\n")
            
            ## im creating a an instance of the object while storing the name of the instance into the data dictionary where it will be assigned a key that can be called upon
            instance_names[temp_name] = Heavy_Equipment(temp_name, "heavy", temp_brand, temp_description, temp_fuel, None) 
            ##print(jack.name)
            # print(temp_name.type)
            # print(temp_name.brand)
            # print(temp_name.description)
            # print(temp_name.fuel_type)
            if temp_renting_status == "yes":
                client_name = input("what is the client's name?\n")
                client_address = input("what is the client's address?\n")
                client_phone_no = input("what is the client's phone number?\n")
                start_date = input("what is the renting start date?\n")
                end_date = input("what is the end date?\n")
            #   temp_name.allocate(client_name, client_address, client_phone_no, start_date, end_date)        ## this is being used to test if the data has been added to the data
            # for x in temp_name.renting_status.values():                                                       ## has been added to the data dictionary  
            #     print(x)
            else:
                instance_names[temp_name].unallocate
        else:
            answer_2 = input("would you like to alter the details of a pre-existing entry?\n")
            if answer_2 == "yes":
                temp_name = input("Please anter the name of the item you would like alter\n")
                print("Name:",instance_names[temp_name].name)
                print("Type:",instance_names[temp_name].type)
                print("Brand:",instance_names[temp_name].brand)
                print("Equipment description:",instance_names[temp_name].description)
                print("Fuel Type:",instance_names[temp_name].fuel_type)
                
                
                
            

                
                
                
        
        
    


        