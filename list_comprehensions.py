# this program creates a random list of specified size and creates a new list containing the even elements


import random


def get_even_elements(a):
    return [i for i in a if i % 2 == 0]


if __name__ == '__main__':
    population = range(0, 100)
    a = random.sample(population, 10)
    print(a)

    print(get_even_elements(a))