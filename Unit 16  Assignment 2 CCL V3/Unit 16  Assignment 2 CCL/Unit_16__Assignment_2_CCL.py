from heavy_equipment import Heavy_Equipment
from small_equipment import Small_Equipment



def renting_details_getter():
    temp_name = input("what is the name of the Equipment you would like to alter?\n")
    client_name = input("what is the client's name?\n")
    client_address = input("what is the client's address?\n")
    client_phone_no = input("what is the client's phone number?\n")
    start_date = input("what is the renting start date?\n")
    end_date = input("what is the end date?\n")
    instance_names[temp_name].allocate(client_name, client_address, client_phone_no, start_date, end_date) 
    
def heavyequipment_details_getter():
    temp_name = input("What is the name of the Equipment?\n")
    temp_brand = input("What is the Brand?\n")
    temp_description = input("Please provide a breif description of the product\n")
    temp_fuel = input("what is the fuel type\n")
    temp_renting_status = input("Is it being rented? If rented please enter yes, and if it is not then please enter N/a. Thank you!\n")
    temp_name = Heavy_Equipment(temp_name, "heavy", temp_brand, temp_description, temp_fuel, None)
    

def number_validator(place_holder):
    place_holder.strip()
    while place_holder == "" or place_holder.isdigit() == False:
        place_holder = input("you have not entered a value or you have not your input was not a digit please re-enter your input\n")
    return place_holder

def word_validator(place_holder):
    place_holder.strip()
    place_holder.lower()
    while place_holder == "" or place_holder.isalpha() == False:
        place_holder = input("you have not entered a value or your input was not completely word and contained numbers init, please re-enter your input\n")
    place_holder.strip()
    place_holder.lower()
    return place_holder
    
    
    
# def program_closer():
#     close_program_input = input("would you like to close the program")
#     if close_program_input == "close":
#         break
#  #    else:
#  #        continue

instance_names = {}    ## i am creating another data dictionary to try and name my objects dynamically based on the name 
                       ## that the user have input for the equipment. this creates a dynamic naming system based on user inputs 

# print("Name:",instance_names[temp_name].name)
# print("Type:",instance_names[temp_name].type)
# print("Brand:",instance_names[temp_name].brand)
# print("Equipment description:",instance_names[temp_name].description)
# print("Fuel Type:",instance_names[temp_name].fuel_type)



## im importing the both of the classes that i have create and from their respective programs
loop = True 
while loop == True:
    print("welcome to Construction Corporation's Equipment mangemnt software")
    answer_1 =  input("What would you like to do? \nIf regarding heavy equipment please enter 1 \nIf regarding small equipment please type 2\nIf you would like to quit the program please enter 3\n")
    ##this is an input which can only have three inputs so i am making sure that the user can only input one of three options for the code to work 
    while answer_1 == "":
        answer_1 = input("you have not provided an input\n")
    answer_1 = number_validator(answer_1)
    # int(answer_1)
    while answer_1 != "1" and answer_1 != "2" and answer_1 != "3":
        answer_1 = input("you have not provided an answer that is between 1 and 3, please re-enter your answer\n")
    # while answer_1 == "" or answer_1.isalpha() == "false":
    #     answer_1 = input("you have not entered a value or you have not your input was not a digit please re-enter your input\n")
    if answer_1 == "1":
        answer_2 = input("would you like to add a new heavy construction equipment\n")
        answer_2 = word_validator(answer_2)
        if answer_2 == "yes":
            temp_name = input("What is the name of the Equipment?\n")
            temp_name= word_validator(temp_name)
            temp_brand = input("What is the Brand?\n")
            temp_brand = word_validator(temp_brand)
            temp_description = input("Please provide a breif description of the product\n")
            ##temp_description = word_validator(temp_description)
            temp_fuel = input("what is the fuel type\n")
            temp_fuel = word_validator(temp_fuel)
            temp_renting_status = input("Is it being rented? If rented please enter 'yes', and if it is not then please enter 'n/a'. Thank you!\n")
            ## this is a unique field with only 2 options that can be selected so a unique validation technique will be added
            temp_renting_status.strip()
            temp_renting_status = temp_renting_status.lower()
            while temp_renting_status != "yes" and temp_renting_status != "n/a":
                temp_renting_status = input("you have not provided an suitable input please use the examples provided above, re-input your answer")
            temp_renting_status.strip()
            temp_renting_status = temp_renting_status.lower()           
            ## im creating a an instance of the object while storing the name of the instance into the data dictionary where it will be assigned a key that can be called upon
            instance_names[temp_name] = Heavy_Equipment(temp_name, "heavy", temp_brand, temp_description, temp_fuel, None) 
            #print(instance_names{jack}.name)
            # print(temp_name.type)
            # print(temp_name.brand)
            # print(temp_name.description)
            # print(temp_name.fuel_type)
            if temp_renting_status == "yes":
                client_name = input("what is the client's name?\n")
                # client_name = word_validator(client_name)
                client_address = input("what is the client's address?\n")
                # client_address = word_validator(client_address)
                client_phone_no = input("what is the client's phone number?\n")
                # client_phone_no  = word_validator(client_phone_no)
                start_date = input("what is the renting start date?\n")
                # start_date = word_validator(start_date)
                end_date = input("what is the end date?\n")
                # end_date = word_validator(end_date)
                instance_names[temp_name].allocate(client_name, client_address, client_phone_no, start_date, end_date)
       ## this is being used to test if the data has been added to the data
            # for x in instance_names[temp_name].renting_status.values():                                                       ## has been added to the data dictionary  
            #     print(x)
                print("n\n\n")    
            else:
                instance_names[temp_name].unallocate
                print("\n\n\n")
        elif answer_2 == "no" :
            answer = input("would you like to alter the renting status of some equipment?\n")
            answer = word_validator(answer)
            if answer == "yes":
                answer_3 = input("would you like to unallocate or allocate the renting status?\n")
                answer_3 = word_validator(answer_3)
                if answer_3 == "allocate":
                    renting_details_getter()
                    print("\n\n\n")
                elif answer_3 == "unallocate":
                    temp_name = input("what is the name of the Equipment you would like to alter?\n")
                    temp_name = word_validator(temp_name)
                    instance_names[temp_name].unallocate
            elif answer_2 == "no":
                answer = input("would you like to cheack the details of a piece of equipment\n")
                if answer == "yes":
                    answer = word_validator(answer)
                    temp_name = input("what is the name of the Equipment?\n")
                    #answer = input("is it being rented")
                    print("the product's Name is:",instance_names[temp_name].name)
                    print("the product Type is:",instance_names[temp_name].type)
                    print("the product Brand is:",instance_names[temp_name].brand)
                    print("the product Description is:",instance_names[temp_name].description)
                    print("This product uses:",instance_names[temp_name].fuel_type)

                    if instance_names[temp_name].renting_status == None:
                        print("\n\n\n")
                        continue
                    else:
                        for x in instance_names[temp_name].renting_status.values():  
                            print(x)
                        print("\n\n\n")
                    
                elif answer == "no":
                    answer = input("input would you like to end the program")
                    answer = word_validator(answer)
                    if answer == "yes":
                        break
    elif answer_1 == "2":
        answer_2 = input("would you like to add a new Small equipment\n")
        answer_2 = word_validator(answer_2)
        if answer_2 == "yes":
            temp_name = input("What is the name of the Equipment?\n")
            temp_name = word_validator(temp_name)
            temp_brand = input("What is the Brand?\n")
            temp_brand = word_validator(temp_brand)
            temp_description = input("Please provide a breif description of the product\n")
            temp_desciption = word_validator(temp_description)
            temp_quantity = input("what is the products current stock/quantity type\n")
            temp_quantity = number_validator(temp_quantity)
            temp_price = input("what is the products current price?")
            temp_price = number_validator(temp_price)
            instance_names[temp_name] = Small_Equipment(temp_name, "heavy", temp_brand, temp_description, temp_quantity, temp_price)
            print("\n\n\n")
        elif answer_2 == "no":
            answer = input("would you like to change the price or quantity of a small equipment?\n(Example: if price then please input 'price', if neither then please answer 'no')\n")
            answer = word_validator(answer)
            if answer == "price":
                temp_name = input("what is the name of the small equipments price that you would want to change")
                temp_name = word_validator(temp_name)
                temp_price = input("what is the new price?")
                temp_price = number_validator(temp_price)
                instance_names[temp_name].update_price(temp_price)
                print("the product's Name is:",instance_names[temp_name].name)
                print("the product Type is:",instance_names[temp_name].type)
                print("the product Brand is:",instance_names[temp_name].brand)
                print("the product Description is:",instance_names[temp_name].description)
                print("This products current quanitty is:",instance_names[temp_name].quantity)
                print("This products new price is:",instance_names[temp_name].price,"\n\n\n")
            elif answer == "quantity":
                temp_name = input("what is the name of the small equipments price that you would want to change\n")
                temp_name = word_validator(temp_name)
                temp_quantity = input("what is the new quantity?")
                temp_quantity = number_validator(temp_quantity)
                instance_names[temp_name].update_quantity(temp_price)
                print("the product's Name is:",instance_names[temp_name].name)
                print("the product Type is:",instance_names[temp_name].type)
                print("the product Brand is:",instance_names[temp_name].brand)
                print("the product Description is:",instance_names[temp_name].description)
                print("This products current quanitty is:",instance_names[temp_name].quantity)
                print("This products quanitty price is:",instance_names[temp_name].price,"\n\n\n")
            elif answer == "no":
                answer = input("would you like to cheack the details of a piece of equipment\n")
                answer = word_validator(answer)
                if answer == "yes":
                    temp_name = input("what is the name of the Equipment?\n")
                    instance_names[temp_name].PrintDetails(instance_names[temp_name].name, "small", instance_names[temp_name].brand, instance_names[temp_name].description, instance_names[temp_name].quantity, instance_names[temp_name].price)

                    # print("the product's Name is:",instance_names[temp_name].name)
                    # print("the product Type is:",instance_names[temp_name].type)
                    # print("the product Brand is:",instance_names[temp_name].type)
                    # print("the product Description is:",instance_names[temp_name].description)
                    # print("This products current quanitty is:",instance_names[temp_name].quantity)
                    # print("This products quanitty price is:",instance_names[temp_name].price,"\n\n\n")
                elif answer == "no":
                    answer = input("input would you like to end the program")
                    if answer == "yes":
                        break
    elif answer_1 == "3":
            break