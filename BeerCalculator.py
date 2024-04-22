# Function to calculate MCU
def calculate_mcu():
    malt_mcu_values = []  # List to store partial MCU values for each malt
    total_mcu = 0
    malt_name = ""
    beer_name = input("Let's give your beer a name: ")
    f_vol = float(input("Inform final volume: "))

    print("Enter malt information (type 'q' to finish): ")
    while True:
        malt_name = input("Malt name: ")
        
        if malt_name == "q":
            break
        
        grain_weight = float(input("Weight (kg) of {}: ".format(malt_name)))
        l_degrees = float(input("ºL (Degrees Lovibond) of {}: ".format(malt_name)))

        # Calculating the partial MCU (Malt Colour Units)
        mcu = (grain_weight * (l_degrees * 2.205) / (f_vol * 0.264))
        
        # Append the partial MCU value to the list
        malt_mcu_values.append((malt_name, mcu))
        
        # Each time the MCU is calculated, it is added to the total_mcu
        total_mcu += mcu
    
    # Display partial MCU values for each malt
    print("\nPartial MCU values:")
    for malt, mcu in malt_mcu_values:
        print("MCU for {}: {:.2f} SRM".format(malt, mcu, mcu))
    
    # Display total MCU
    print("\nTotal MCU for {}: {:.2f} SRM".format(beer_name, total_mcu))


# Function to convert units
def convert_units():
    # Initializing values
    EBC = 0
    SRM = 0
    L = 0
    
    value_2_be_converted = float(input("Type the value you want to convert: "))
    user_input = input("\n \n Choose your unit!: \n 1 - EBC -> SRM \n 2 - SRM -> EBC \n 3 - ºL -> SRM \n 4 - SRM -> ºL: \n 5 - EBC -> ºL:\n ")

    if user_input == "1":
        # EBC -> SRM
        EBC = value_2_be_converted
        SRM = EBC * 0.508

    elif user_input == "2":
        # SRM -> EBC
        SRM = value_2_be_converted
        EBC = SRM * 1.97
    
    elif user_input == "3":
        # ºL -> SRM
        L = value_2_be_converted
        SRM = (1.3546 * L) - 0.76

    elif user_input == "4":
        # SRM -> ºL 
        SRM = value_2_be_converted
        L = (SRM + 0.76) / 1.3546
    
    elif user_input == "5":
        # EBC -> ºL 
        EBC = value_2_be_converted
        SRM = EBC * 0.508
        L = (SRM + 0.76) / 1.3546
        
    else:
        print("Invalid input. Enter a number between 1 and 5")
        return

    # Print the result
    print("Converted value:")
    if user_input == "1" or user_input == "3":
        print("SRM:", SRM)
    elif user_input == "2":
        print("EBC:", EBC)
    elif user_input == "4":
        print("ºL:", L)
    elif user_input == "5":
        print("ºL:", L)
        
# calculating the malt quantity necessary

# Main menu
while True:
    print("\nMenu:")
    print("a. Calculate MCU")
    print("b. Convert Units")
    print("c. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "a":
        calculate_mcu()
    elif choice == "b":
        convert_units()
    elif choice == "c":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
