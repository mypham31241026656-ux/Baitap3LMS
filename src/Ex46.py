# 46. Write a Python program to select the odd items from a list.
list = [2,3,4,5,6,7,8]
result = []
for item in list:
    if item % 2 !=0:
        result.append(item)
print(result)