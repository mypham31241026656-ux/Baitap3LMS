# 2. Write a Python program to multiply all the items in a list.
import random

lst = []
for i in range(20):
    lst.append(random.randint(1,50))

def print_list():
    print(lst)

def ex_02():
    product = 1
    for item in lst:
        product *= item
    print(f"Production of item: {product}")

if __name__ == '__main__':
    print_list()
    ex_02()