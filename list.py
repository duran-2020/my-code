import random
wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

choice= int(input("Pick a student number!"))
student_name= tlgstudents[choice]


print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.')

print("\n //// Randomized Student Name section //// \n")

choice = random.randint(0,19)
student_name = tlgstudents[choice]

print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.')

