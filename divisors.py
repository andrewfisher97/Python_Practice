# This program takes a number from the user and returns all of its divisors


def find_divisors(num):
    potential_divisors = range(1, num+1)
    divisors = []

    for i in potential_divisors:
        if num % i == 0:
            divisors.append(i)

    return divisors


if __name__ == '__main__':
    user_number = int(input("Enter a number: "))

    print(find_divisors(user_number))