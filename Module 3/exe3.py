print("Hello!")

gender = input("Enter your gender: ")
h_value = int(input("Enter your haemoglobin value in g/l: "))

if (gender == "Male") or (gender == "male"):
    if h_value < 134:
        print("Your haemoglobin value is low!!!")
    elif (h_value >= 134) and (h_value <= 167):
        print("Your haemoglobin value is normal.")
    else:
        print("Your haemoglobin value is high!!!")
else:
    if h_value < 117:
        print("Your haemoglobin value is low!!!")
    elif (h_value >= 117) and (h_value <= 155):
        print("Your haemoglobin value is normal.")
    else:
        print("Your haemoglobin value is high!!!")