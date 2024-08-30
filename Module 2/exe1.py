print("Hello!")
length = int(input("Enter the length of the zander in centimeters : "))
length_rem = 42 - length
if length < 42:
    print("Release the fish back into the lake. \nThe fish you caught is" ,length_rem,"cm below the size limit.")
else:
    print("The length you entered meets the size limit.")