number = 1

while number <= 1000:
    rem = number % 3
    if rem == 0:
        print(number)
        number +=1
    else:
        number += 1
print("These are the numbers from 1-1000 which are divisible by 3.")