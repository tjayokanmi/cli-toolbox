def celsius_to_fahrenheit(cel):
    return (cel * 1.8) + 32

def fahrenheit_to_celsius(fah):
    return (fah - 32) * (5/9)

def unit_converter():
    print("""
    Unit Converter

    1. Celsius → Fahrenheit
    2. Fahrenheit → Celsius
    """)

    opt = input("Choose conversion: ")

    if opt == "1":
        cel = float(input("Enter temperature: "))
        result = celsius_to_fahrenheit(cel)
        print("The result is: " + str(result) + " Fahrenheit")
    elif opt == "2":
        fah = float(input("Enter temperature: "))
        result = fahrenheit_to_celsius(fah)
        print("The result is: " + str(round(result, 4)) + " Celsius")
    else:
        print("You have selected an invalid option...")