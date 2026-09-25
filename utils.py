def get_number(prompt):
    
    while True: 
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Enter a valid number")
    return number       
