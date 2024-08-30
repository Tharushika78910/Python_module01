length = int(input("Enter a length in inches : "))
while length > 0:
    length_cm = length * 2.54
    print("The entered length in centimeters : ",length_cm,"cm")
    length = int(input("Enter a length in inches : "))
print("The entered length is not valid!")
