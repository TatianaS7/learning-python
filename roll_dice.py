import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll:\n"))

if roll == guess:
    print("You're correct! The computer rolled a " + str(roll))
else: 
    print("Wrong! The computer rolled a " + str(roll))