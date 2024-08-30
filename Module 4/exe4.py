import random
number = random.randint(1,10)
print("Computer has drawn the number.\nNow it's time to you to guess the number.")
guess = int(input("Guess the number : "))
while guess != number:
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Guess again : "))
print("Your guess is correct!!!")
