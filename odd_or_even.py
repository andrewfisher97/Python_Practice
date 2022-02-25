# this program takes a user input number and determines whether it is even or odd and checks to see if it is a
# multiple of four
# it also checks to see, given two numbers, if one number can be divided by another number evenly


def multiple_of_four(num):
    if num % 4 == 0:
        print("The number is a multiple of four.")
    else:
        print("The number is not a multiple of four.")


def even_or_odd(num):
    if num % 2 > 0:
        print("The number is odd.")
    else:
        print("The number is even.")


def check_division(num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}!")
    else:
        print(f"{num1} is not divisible by {num2}!")


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    even_or_odd(number)
    multiple_of_four(number)

    num_to_check = int(input("Enter number to check: "))
    num_to_divide = int(input("Enter number to divide number to check by: "))
    check_division(num_to_check, num_to_divide)
