from utils import get_number

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

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
        celsius = get_number("Enter Temperature: ")
        result = celsius_to_fahrenheit(celsius)
        print("The result is: " + str(result) + " Fahrenheit")
        print()
        
    elif opt == "2":
        fahrenheit = get_number("Enter Temperature: ")
        result = fahrenheit_to_celsius(fahrenheit)
        print("The result is: " + str(round(result, 2)) + " Celsius")
        print() 
    elif opt == "3":    
       
        km = get_number("Enter Kilometres: ")
        result = kilometers_to_miles(km)
        print("The result is: " + str(round(result, 2)) + " Miles")
        print()
 
    elif opt == "4":
        miles = get_number("Enter Miles: ")
        result = miles_to_kilometres(miles)
        print("The result is: " + str(round(result, 2)) + " Kilometers")
        print()
            
    elif opt.upper() == "X": 
        print("You have decided to exit the unit converter")
        
    else:
        print("You have selected an invalid option...")
