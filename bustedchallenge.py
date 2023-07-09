#!/usr/bin/env python3

def main():
    # Dictionary mapping numbers to corresponding words
    words = {
        1: "great",
        2: "fabulous",
        3: "super"
    }

    while True:
        # Prompt the user for their name
        name = input('What is your name?\n>')

        # Prompt the user for a number and convert it to an integer
        num = int(input("Pick a number between 1 and 3: "))

        if name and num in words.keys():
            # If both name and number are valid, display a personalized message
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break  # Exit the loop
        else:
            # If either name or number is invalid, display an error message
            print("Come on, follow directions. Try again.")

# Call the main function to start the program
main()

