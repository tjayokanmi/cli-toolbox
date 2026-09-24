from unit_converter import get_number

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
        while True:
            try: 
                x = get_number("Enter the first number: ")
                y = get_number("Enter the second number: ")
                break
            except ValueError:
                print("Kindly enter a number")
                
        if option == "1":
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(addition(x,y))
        elif option == "2":
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(subtraction(x,y))
        elif option == "3":
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(multiplication(x,y))
        elif option == "4":
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            while True:
                try: 
                    y = float(input("Enter the second number: "))
                    result = division(x,y)
                    print(result)
                    break
                except ZeroDivisionError:
                    print("Invalid Division Operation \n The second number cannot be zero")
                except ValueError:
                    print("Kindly enter a number")

        
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
    
   

