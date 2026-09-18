def to_fah(cel):
    return (cel * 1.8) + 32

def to_cel(fah):
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
        result = to_fah(cel)
        print("The result is: " + str(result) + " Fahreheit")
    elif opt == "2":
        fah = float(input("Enter temperature: "))
        result = to_cel(fah)
        print("The result is: " + str(round(result, 4)) + " Celsius")