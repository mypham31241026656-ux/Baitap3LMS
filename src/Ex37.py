# 37. Write a Python program to find common items in two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6,3]
common_items = list(set(list1)&set(list2))
print("List1: ", list1)
print("List2: ", list2)
print("common_items: ", common_items)

list1 = [1, 2, 3]
list2 = [4, 5, 6,3]
common_items =[]
for item in list1:
    if item in list2:
        common_items.append(item)
print("common_items: ", common_items)