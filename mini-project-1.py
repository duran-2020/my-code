#!usr/bin/env python3

# Free Time Activity Suggestion Program
# This program asks the user a series of questions with two options each
# Based on the user's responses, it suggests an activity for their free time

# Ask the user multiple-choice questions
name = input("Hello! Please enter your name: ")

print(f"\nWelcome {name}! Let's find out what you can do with your free time.\n")
print("Please answer the following questions by entering the corresponding number.\n")

# Function to validate user input
def validate_input(prompt, valid_options):
    while True:
        response = input(prompt)
        if response in valid_options:
            return response
        else:
            print("\nInvalid input. Please enter a valid option.\n")

# Question 1
response1 = validate_input("Do you prefer indoor or outdoor activities?\n"
                           "   1. Indoor\n"
                           "   2. Outdoor\n",
                           ["1", "2"])

# Question 2
response2 = validate_input("Are you in the mood for something active or relaxing?\n"
                           "   1. Active\n"
                           "   2. Relaxing\n",
                           ["1", "2"])

# Determine activity based on user's responses
if response1 == "1" and response2 == "1":
    activity = "Go for a workout at the gym."
elif response1 == "1" and response2 == "2":
    activity = "Read a book or watch a movie at home."
elif response1 == "2" and response2 == "1":
    activity = "Take a hike or go for a run in nature."
elif response1 == "2" and response2 == "2":
    activity = "Visit a park or have a picnic outside."
else:
    activity = "Hmm, I'm not sure. Maybe you can explore a new hobby or spend time with friends."

# Provide activity suggestion based on the user's responses
print(f"Based on your preferences {name}, I suggest you:", activity)
