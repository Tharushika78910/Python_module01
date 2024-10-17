name = set()

while True:
    your_name = input("Enter your name:")

    if your_name =="":
        break

    if your_name in name:
        print("Existing name")
    else:
        print("New name")
        name.add(your_name)

print("\nAll names entered:")
for your_name in name:
    print(your_name)