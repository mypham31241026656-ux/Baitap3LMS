# 29. Write a Python program to get unique values from a list.ê

def unique_numbers(nums):
    unique = list(set(nums))
    print("The unique numbers are: ", unique)

nums =[3,5,9,1,3,5,9,8,8,1,2,3,1]
unique_numbers(nums)