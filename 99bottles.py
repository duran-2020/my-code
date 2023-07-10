#!/usr/bin/env python3

# Define the maximum number of bottles
max_bottles = 100

# Keep running the loop until a valid input or 'q' is provided
while True:
    num_bottles = input("How many bottles of beer are on the wall? (1-100) (q to quit): ")

    # Check if the user wants to quit
    if num_bottles.lower() == 'q':
        print("Goodbye!")
        break

    try:
        num_bottles = int(num_bottles)
        
        # Check if the input is within the valid range
        if num_bottles < 1 or num_bottles > max_bottles:
            print("Invalid input! Please enter a number between 1 and 100.")
        else:
            # Generate the song lyrics based on the number of bottles
            for i in range(num_bottles, 0, -1):
                print(f"{i} bottles of beer on the wall!")
                print(f"{i} bottles of beer! You take one down, pass it around!")
                
                # Check if the next line should display "bottle" or "bottles"
                if i - 1 == 1:
                    print(f"{i - 1} bottle of beer on the wall!")
                elif i - 1 == 0:
                    print("No more bottles of beer on the wall!")
                else:
                    print(f"{i - 1} bottles of beer on the wall!")
                print()
            
            break
    except ValueError:
        print("Invalid input! Please enter a number or 'q' to quit.")

