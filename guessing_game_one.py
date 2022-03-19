# this program generates a random number between 1 and 9 and the user guesses until they get the correct number.
# the program keeps track of guess count and number of rounds and displays it to the user.
# the program uses validation and error handling to keep gameplay smooth.


import random


def check_guess(rand, guess):
    if guess == rand:
        print("You guessed correct! YOU WIN!")
        return 1
    else:
        if guess > rand:
            print("Too high. Guess again.")
            return 0
        else:
            print("Too low. Guess again.")
            return 0


def get_user_guess():
    guess = input("Enter your guess: ")

    if guess.lower() == 'exit':
        print("Game over.")
        quit()

    try:
        int(guess)
    except ValueError:
        return 0

    if 1 <= int(guess) <= 9:
        return int(guess)
    else:
        return 0


if __name__ == '__main__':
    round_count = 0
    random_number = random.randint(1, 9)

    print("Guess should be a number between 1-9.")
    print("Enter 'exit' to end.")

    while True:
        guess_count = 0
        round_count += 1
        print(f"Round {round_count}")

        while True:
            user_guess = get_user_guess()
            guess_count += 1

            while True:
                if user_guess != 0:
                    break
                else:
                    print("Guess is out of bounds. Guess again.")
                    user_guess = get_user_guess()

            if check_guess(random_number, user_guess) == 1:
                print(f"Number of guesses: {guess_count}")
                random_number = random.randint(1, 9)
                break
