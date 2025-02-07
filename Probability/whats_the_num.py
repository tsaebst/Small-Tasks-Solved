''' "Guess the Number" is a classic game.

In this game, the computer thinks of a random number between 1 and 100.

The player has 10 chances to guess the number.

After each guess, the computer tells the player whether their number is higher or lower than the secret number.

At the end, the number of attempts taken to guess correctly is displayed. '''

import random


def check(a, b):
    if a == b:
        print("Congrats! Now you know the number.")
        return True
    if a > b:
        print("Oops! Your number is a little bit smaller than mine.")
    elif a < b:
        print("Oops! Your number is a little bit greater than mine.")
    return False


def guess():
    number = random.randint(1, 100)
    print("I created a number! Small hint - it's in the range from 1 to 100.")
    attempts = 10
    while attempts != 0:
        try:
            guess_try = int(input(f"You have {attempts} attempt(s) to guess the number I created. Enter your assumption: "))
        except ValueError:
            print("You've entered a non-numeric value. Please enter an integer.")
            continue
        if_true = check(guess_try, number)
        if not if_true:
            attempts -= 1
        else:
            print(f"You did it in {10 - attempts + 1} attempt(s)!")
            break
    else:
        print(f"Sorry, you've run out of attempts! The number was {number}.")


guess()
