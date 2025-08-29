# 18. Write a Python program to generate all permutations of a list in Python.
import itertools

data = [1,2,4]
perm = list(itertools.permutations(data))
print('ALl permutations: ')
for p in perm:
    print(p)