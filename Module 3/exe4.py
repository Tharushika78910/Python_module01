print("Hello!")

year = int(input("Enter a year: "))
rem1 = year % 4         #remaining after divided by 4
rem2 = year % 100       #remaining after divided by 100
rem3 = year % 400       #remaining after divided by 400

if rem1 == 0:
    if (rem2 == 0) and (rem3 == 0):
        print("The year",year," is a leap year.")
    elif (rem2 == 0) and (rem3 != 0):
        print("The year",year," is not a leap year.")
    else:
        print("The year",year," is a leap year.")
else:
    print("The year",year," is not a leap year.")