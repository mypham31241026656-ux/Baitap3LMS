# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
# 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
nested_list = []

for i in range(len(colors)):
    nested_list.append({"color_name": {colors[i]}, "Color_code":codes[i]})

for item in nested_list:
    print(item)
