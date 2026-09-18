While True: 
    print("""=== Command-Line Toolbox ===

    1. Unit Converter
    2. Calculator
    3. Number Guessing Game
    4. Exit
    """)

    option = input("Choose an option: ")

    if option == "1":
        print("You choose a Unit Converter")
        #lauch Unit Converter

    elif option == "2":
        print("You choose a Calculator")
        #launch Calculator

    elif option == "3":
        print("You choose a Number Guessing Game")
        #launch Number Guessing Game
    elif option == "4":
        print("You choose to exit the CLI Toolbox")
        #exit cli toolbox 
    else: 
        print("You hve selected an invalid option.\n Kindly choose from 1 - 3 baseed on your preference")
        