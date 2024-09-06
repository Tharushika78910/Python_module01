import random
number = int(input("How many dice do you want to roll? "))
i=0
result_list = []
for i in range(number):
    result = random.randint(1,6)
    result_list.append(result)
    i += 1
total = sum(result_list)
print("Sum of the results :",total)