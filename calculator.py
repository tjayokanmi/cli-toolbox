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

     
    if option.upper() == "X":
        return
    elif option in ("1", "2", "3", "4"):
        try: 
             x = float(input("Enter the first number: "))
             y = float(input("Enter the second number: "))
        except ValueError:
            return "Kindly enter a number"

        if option == "1":
            print(addition(x,y))
        elif option == "2":
            print(subtraction(x,y))
        elif option == "3":
            print(multiplication(x,y))
        elif option == "4":
            try: 
                print(division(x,y))
            except ZeroDivisionError:
                print("Invalid Division Operation")

        
    else:
        print("You have entered an invalid option") 

def addition(x, y):
    return x + y
    
def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y 
   

calculator()