#!/usr/bin/env python3

# Set the initial round number to 0
round = 0

# Start an infinite loop
while True:
    # Increase the round number by 1
    round = round + 1
    
    # Print the question for the movie title
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    
    # Get user input for their guess
    answer = input("Your guess --> ")
    
    # Check if the answer is correct
    if answer == 'Brian':
        print('Correct')
        # If the answer is correct, exit the loop
        break
    
    # Check if the maximum number of rounds (3) has been reached
    elif round == 3:
        print("Sorry, the answer was Brian.")
        # If the maximum rounds have been reached, exit the loop
        break
    
    # If the answer is incorrect and the maximum rounds have not been reached
    else:
        print("Sorry, Try again!")

