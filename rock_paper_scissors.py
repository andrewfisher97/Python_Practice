# this program takes two user inputs which indicate rock, paper, or scissors and simulates the game


def determine_winner(p1, p2):
    if p1 == 'rock' and p2 == 'rock':
        return ''
    elif p1 == 'rock' and p2 == 'paper':
        return 'Player 2'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1'
    elif p1 == 'paper' and p2 == 'paper':
        return ''
    elif p1 == 'paper' and p2 == 'scissors':
        return 'Player 2'
    elif p1 == 'scissors' and p2 == 'rock':
        return 'Player 2'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1'
    elif p1 == 'scissors' and p2 == 'scissors':
        return ''


if __name__ == '__main__':

    print("Each player should enter 'rock', 'paper', or 'scissors'.")
    print("Enter 'stop' to end the game.")

    while True:

        while True:
            user_choice_a = input("Player 1 - Enter your choice: ")
            if user_choice_a == 'stop':
                quit()
            elif user_choice_a in ('rock', 'paper', 'scissors'):
                break
            else:
                print("Invalid response: please enter 'rock', 'paper', or 'scissors'.")

        while True:
            user_choice_b = input("Player 2 - Enter your choice: ")
            if user_choice_b == 'stop':
                quit()
            elif user_choice_b in ('rock', 'paper', 'scissors'):
                break
            else:
                print("Invalid response: please enter 'rock', 'paper', or 'scissors'.")

        winner = determine_winner(user_choice_a, user_choice_b)
        if winner == '':
            print("Tie! Go again.")
        else:
            print(f'{winner} wins!')