def celsius_to_fahrenheit(cel):
    return (cel * 1.8) + 32

def fahrenheit_to_celsius(fah):
    return (fah - 32) * (5/9)

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometres(miles):
    return miles * 1.60934

def unit_converter():
    print("""
    Unit Converter

    1. Celsius → Fahrenheit
    2. Fahrenheit → Celsius
    3. Kilometers → Miles
    4. Miles → Kilometers
    X. Exit Unit Converter
    """)

    opt = input("Choose conversion: ")

    if opt == "1":
        cel = float(input("Enter temperature: "))
        result = celsius_to_fahrenheit(cel)
        print("The result is: " + str(result) + " Fahrenheit")
        print() 

    elif opt == "2":
        fah = float(input("Enter temperature: "))
        result = fahrenheit_to_celsius(fah)
        print("The result is: " + str(round(result, 2)) + " Celsius")
        print() 

    elif opt == "3":
        km = float(input("Enter Kilometres: "))
        result = kilometers_to_miles(km)
        print("The result is: " + str(round(result, 2)) + " Miles")
        print() 
    elif opt == "4":
        miles = float(input("Enter Miles: "))
        result = miles_to_kilometres(miles)
        print("The result is: " + str(round(result, 2)) + " Kilometers")
        print()
    elif opt == "X": 
        print("You have decided to exit the unit converter")
        
    else:
        print("You have selected an invalid option...")
