#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num = random.randint(1, 100)

    rounds = 0

    while rounds < 5:
        guess = input("Guess a number between 1 and 100\n>")

        if guess.isdigit():
            guess = int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("Correct!")
            break  # Exit the loop if the guess is correct

        rounds += 1  # Increment rounds by 1 after each guess

    if rounds == 5 and guess != num:
        print("Out of chances! The number was", num)

# Call the main function to start the game
main()

