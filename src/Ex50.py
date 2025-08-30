# 50. Write a Python program to sort a list of nested dictionaries
list = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20}]
sorted_list = sorted(list, key=lambda x: x["name"])
for item in sorted_list:
    print(item)