numbers = []
num = input("Enter a number or press enter to quit: ")

while num != "":
    numbers.append(num)
    num = input("Enter the next number or press enter to quit: ")

for num in range(len(numbers)):
    numbers[num] = int(numbers[num])

num_sort = sorted(numbers, reverse=True)
print(f"Five maximum numbers are: "+str(num_sort[:5]))