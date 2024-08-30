talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots= float(input("Enter the number of lots: "))

gram = (talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)
kilogram = int(gram/1000)
gram_rem = float(gram%1000)

print("The weight in modern units:")
print(kilogram,f"kilograms and {gram_rem:.2f}", "grams")