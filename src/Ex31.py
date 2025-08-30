# 31. Write a Python program to count the number of elements in a list within a
# specified range.
#đếm số phần tử trong list nằm trong một khoảng giá trị cho trước (min, max).

def count_in_range(numbers, min_value, max_value):
    count = 0
    for num in numbers:
        if min_value <=num<=max_value:
            count+=1
    print("The numbers in range: ", count)

nums = [4,9,3,6,8,3,4,9,8,11,1,1]
count_in_range(nums, 0, 100)