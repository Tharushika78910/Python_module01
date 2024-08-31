username = input("User Name: ")
password = input("Password: ")
i = 0

while (username != "python" or password != "rules") and i<5:
    i = i + 1
    if i<5:
        print("Enter Username and Password again.")
        username = input("User Name: ")
        password = input("Password: ")
    else:
        print("Access Denied!")

if username == "python" and password == "rules":
    print("Welcome!!!")