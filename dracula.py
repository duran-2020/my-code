#!/usr/bin/env python3

# Set an initial counter value to 0
counter = 0

# Open the file "dracula.txt" in read mode and assign it to the variable "foo"
with open("dracula.txt", "r") as foo:
    # Open the file "vampytimex.txt" in write mode and assign it to the variable "fang"
    with open("vampytimex.txt", "w") as fang:
        # Iterate over each line in the file "dracula.txt"
        for line in foo:
            # Check if the line contains the word "vampire" (case-insensitive)
            if "vampire" in line.lower():
                # Print the line that contains "vampire"
                print(line)
                # Increase the counter by 1
                counter += 1
                # Write the line to the file "vampytimex.txt"
                fang.write(line)

# Print the final value of the counter
print(counter)

