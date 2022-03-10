# this program


import random


def check_guess(rand, guess):
    if guess == 'exit':
        quit()
    elif guess == rand:
        print("You guessed correct! YOU WIN!")
    else:
        print("Guess again.")
        return False

if __name__ == '__main__':
    random_number = random.randint(1, 9)
    guess_count = 0

    print("Guess should be a number between 1-9.")

    while True:
        user_guess = int(input("Enter your guess: "))

        if check_guess(random_number, user_guess):


