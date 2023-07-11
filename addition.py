def addition(num1, num2):
    sum = num1 + num2
    return sum

def main():
    a = int(input('Enter the first interger: '))
    b = int(input('Enter the second interger: '))

    answer = addition(a, b)

    print(f'The sum of {a} and {b} is: {answer}.')

main()
