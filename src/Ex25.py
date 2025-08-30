# 25. Write a Python program to select an item randomly from a list.
import random

list = [6,7,8,9]
for item in list:
    random_item = random.choice(list)
print("After random: ", random_item)