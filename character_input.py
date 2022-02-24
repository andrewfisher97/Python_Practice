# this program asks the user for their name and birth year
# it then prints out a message that tells them the year that they will turn 100 years old
# it also asks them for their favourite number and repeats the message that many times

def year_when_one_hundred(user_birth_year):
    return user_birth_year + 100


if __name__ == '__main__':
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    birth_year = int(birth_year)
    number = input("Enter your favourite number: ")
    number = int(number)

    while number > 0:
        print(f"The year is {year_when_one_hundred(birth_year)} when you are 100 years old!")
        number -= 1
