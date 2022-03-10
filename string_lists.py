# this program gets a user input string and determines whether it is a palindrome or not


def is_palindrome(word):
    reverse = word[::-1]

    if word == reverse:
        return True
    else:
        return False


if __name__ == '__main__':
    user_string = input("Enter a string: ")

    if is_palindrome(user_string):
        print(f"{user_string} is a palindrome!")
    else:
        print(f"{user_string} is not a palindrome!")