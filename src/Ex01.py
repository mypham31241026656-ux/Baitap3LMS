# 1. Write a Python program to sum all the items in a list
import random
from operator import itemgetter

lst = []
for i in range(20):
    lst.append(random.randint(1,50))

def print_list():
    print(lst)

def ex_01():
    sum = 0
    for item in lst:
        sum +=item
    print(f"Sum of item: {sum}")

if __name__ == '__main__':
    print_list()
    ex_01()

