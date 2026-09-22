def calculator():
    print("""
        What do you want to do? 
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        X. Exit
        """)

    option = input("Choose an option: ")

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the first number: "))


    if option == "1":
        print(addition(first_number ,second_number))
    elif option == "2":
        print(subtraction(first_number ,second_number))
    elif option == "3":
        print(multiplication(first_number ,second_number))
    elif option == "4":
        print(division(first_number ,second_number))
    # elif option == "X":
    #     break 
    else:
        print("You have enter an invalid option")


def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y 
