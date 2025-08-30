# 47. Write a Python program to insert an element before each element of a list.

list = [1,2,3,4]
insert_item = "x"
result = []

for item in list:
    result.append(insert_item)
    result.append(item)
print(result)