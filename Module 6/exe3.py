def l_conversion(amount):
    litre = amount * 3.78541
    return litre

gallon = int(input("Enter the amount of American gallons: "))

while True:
    l_conversion(gallon)
    print(f"The amount you entered in litres : {l_conversion(gallon):.2f}")
    gallon = int(input("Enter the amount of American gallons: "))
    if gallon < 0:
        break