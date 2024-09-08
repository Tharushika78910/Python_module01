import random

def dice_roll():
    num = random.randint(1,6)
    return num

while True:
    num_in_dice = dice_roll()
    print("The number got from rolling dice is ", num_in_dice)
    if num_in_dice == 6:
        break