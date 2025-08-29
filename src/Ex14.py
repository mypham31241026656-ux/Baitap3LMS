# 14. Write a Python program to print the numbers of a specified list after removing
# even numbers from it.

list = [2,3,5,78,9,10]
for i in list:
    if i%2==0:
        list.remove(i)
print(list)