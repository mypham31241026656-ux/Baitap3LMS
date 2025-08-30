# 28. Write a Python program to find the second largest number in a list.
def second_largest(number):
    unique_numbers = sorted(set(number))
    if len(unique_numbers) < 2:
        print("It doesn't have second largest number")
    else:
        print("Second largest number: ", unique_numbers[-2])

nums = [4,9,3,6,8]
second_largest(nums)