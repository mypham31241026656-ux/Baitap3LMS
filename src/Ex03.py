# 3. Write a Python program to get the largest number from a list.
import random

lst = []
for i in range(20):
    lst.append(random.randint(1,50))
def print_list():
    print(lst)
def ex_03():
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    print(f"Largest item of the list is: {largest}")

if __name__ == '__main__':
    print_list()
    ex_03()