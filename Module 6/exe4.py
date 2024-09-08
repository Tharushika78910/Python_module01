def list_sum(list1):
    return sum(list1)

user_list = []
num = input("Enter a number or press enter to quit: ")
while num != "":
    user_list.append(int(num))
    num = input("Enter a number or press enter to quit: ")

print(user_list)
print(list_sum(user_list))