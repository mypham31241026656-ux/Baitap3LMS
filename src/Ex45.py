# 45. Write a Python program to convert a pair of values into a sorted unique array.
pair1 = (1,2,3,4,5,8,9)
pair2 = (6,7,8,9,10)
combined = pair1 + pair2
unique_sorted = sorted(set(combined))
print(unique_sorted)