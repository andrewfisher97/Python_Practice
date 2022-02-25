# this program takes a list and finds the elements that are less than five
# it then asks the user for a number and then finds the elements in the list that are less than that number


def find_elements_less_than_five(alist):
    b = []

    for i in alist:
        if i < 5:
            b.append(i)

    print(b)


def find_elements_less_than(alist, num):
    b = []

    for i in alist:
        if i < num:
            b.append(i)

    print(b)


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    find_elements_less_than_five(a)

    number = int(input("Enter a number: "))
    find_elements_less_than(a, number)