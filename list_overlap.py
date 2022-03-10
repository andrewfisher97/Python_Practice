# This program creates two random lists of specified size and creates a new list of common elements


import random


def common_elements(list_a, list_b):
    c = []

    for i in list_a:
        if i in list_b and i not in c:
            c.append(i)

    return c


if __name__ == '__main__':
    population = range(0, 100)

    a = random.sample(population, 5)
    b = random.sample(population, 5)

    print(a)
    print(b)

    print(common_elements(a, b))
