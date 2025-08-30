# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

sample_list = [11,33,50]
result = 0
for num in sample_list:
    digits = len(str(num))
    result = result * (10**digits)+num
print(result)