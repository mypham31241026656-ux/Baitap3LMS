# 38. Write a Python program to change the position of every n-th value to the
# # (n+1)th in a list.
# # Sample list: [0,1,2,3,4,5]
# # Expected Output: [1, 0, 3, 2, 5, 4]
# đổi chỗ vị trí phần tử thứ n với phần tử thứ (n+1) trong list.


sample_list = [0,1,2,3,4,5]
for i in range(0, len(sample_list)-1, 2):
    sample_list[i],  sample_list[i+1] = sample_list[i+1], sample_list[i]
print("Result:  ", sample_list)