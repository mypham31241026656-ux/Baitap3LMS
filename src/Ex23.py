# 23. Write a Python program to flatten a shallow list.

list1 = [[1,2,3],[4,5,6],[7,8,9]]
flattened = []
for l in list1:
    for item in l:
        flattened.append(item)
print("List after flattened: ", flattened)