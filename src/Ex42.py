# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
#tìm phần tử bị thiếu và phần tử thừa giữa hai list.
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

missing = list(set(list1)-set(list2))

additional = list(set(list2)-set(list1))
print(missing)
print(additional)