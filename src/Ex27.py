# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(numbers):
    unique_numbers =sorted(set(numbers)) #set(numbers) loại bỏ các số trùng nhau, sorted(...) sắp xếp tăng dần
    if len(unique_numbers) < 2:
        print("It don't have second smallest number")
    else:
        print("Second smallest number: ", unique_numbers[1])

nums = [6,7,8,9]
second_smallest(nums)