print("""
Unit Converter

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
 """)

opt = input("Choose conversion: ")

def ToFah(cel):
    return (cel * 1.8) + 32

def ToCel(fah):
    return (fah - 32) * (5/9)

if opt == "1":
    cel = float(input("Enter temperature: "))
    result = ToFah(cel)
    print("The result is: " + str(result) + " Fahreheit")
elif opt == "2":
    fah = float(input("Enter temperature: "))
    result = ToCel(fah)
    print("The result is: " + str(round(result, 4)) + " Celsius")