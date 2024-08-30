num = input("Enter numbers: ")
maxi = int(num)
mini = int(num)
while num != "":
    num = int(num)
    maxi = int(max(num,maxi))
    mini = int(min(num,mini))
    num = input()

print("The largest number you entered is :", maxi)
print("The smallest number you entered is :", mini)