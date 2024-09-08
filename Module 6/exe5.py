def sort_even(list_ori):
    list_sorted = []
    for i in range(len(list_ori)):
        if list_ori[i] % 2 == 0:
            list_sorted.append(list_ori[i])
    return list_sorted

user_list = []
num = input("Enter a number or press enter to quit: ")
while num != "":
    user_list.append(int(num))
    num = input("Enter a number or press enter to quit: ")

print("The original list is = ",user_list)
print("The sorted list is = ",sort_even(user_list))