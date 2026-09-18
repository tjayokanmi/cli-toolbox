from unit_converter import unit_converter

while True: 
    
    print("""=== Command-Line Toolbox ===

    1. Unit Converter
    2. Calculator
    3. Number Guessing Game
    4. Exit
    """)

    option = input("Choose an option: ")

    if option == "1":
        print("You choose a Unit Converter")
        unit_converter()
        #lauch Unit Converter

    elif option == "2":
        print("You choose a Calculator")
        #launch Calculator

    elif option == "3":
        print("You choose a Number Guessing Game")
        #launch Number Guessing Game
    elif option == "4":
        print("You chose to exit the CLI Toolbox")
        break
        #exit cli toolbox 
    else: 
        print("You have selected an invalid option.\n Kindly choose from 1 - 4 based on your preference")