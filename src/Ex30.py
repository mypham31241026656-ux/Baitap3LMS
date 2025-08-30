#30. Write a Python program to get the frequency of elements in a list.
#đếm tần suất xuất hiện của các phần tử trong list.

def frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    print("The frequency of numbers are: ", freq)
nums = [4,9,3,6,8,3,4,9,8,11,1,1]
frequency(nums)