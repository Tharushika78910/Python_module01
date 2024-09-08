def best_pizza(diameter,price):
    area = 22/7 * ((diameter/2)**2)
    unit_price = price/area
    return unit_price

price1 = int(input("Enter the price of first pizza: "))
diameter1 = int(input("Enter the diameter of first pizza: "))

price2 = int(input("Enter the price of second pizza: "))
diameter2 = int(input("Enter the diameter of second pizza: "))

if best_pizza(diameter1,price1) > best_pizza(diameter2,price2):
    print("The second pizza provides better value for money!")
elif best_pizza(diameter1,price1) < best_pizza(diameter2,price2):
    print("The first pizza provides better value for money!")
elif best_pizza(diameter1,price1) == best_pizza(diameter2,price2):
    print("Both pizzas are same in price per unit!")