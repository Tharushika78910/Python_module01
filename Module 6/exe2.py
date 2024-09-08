import random

def dice_roll(sides):
    num = random.randint(1, sides)
    return num

n = int(input("Enter number of sides you want in the dice: "))

while True:
    num_in_dice = dice_roll(n)
    print("The number got from rolling dice is ", num_in_dice)
    if num_in_dice == n:
        break