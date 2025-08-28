# 4. Write a Python program to get the smallest number from a list.
import random

lst = []
for i in range(20):
    lst.append(random.randint(1,50))
def print_list():
    print(lst)
def ex_04():
    smallest = lst[0]
    for item in lst:
        if item<smallest:
            smallest = item
    print(f"Smallest item of the list is: {smallest}")

if __name__ == '__main__':
    print_list()
    ex_04()