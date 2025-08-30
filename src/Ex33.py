# 33. Write a Python program to generate all sublists of a list

lst = [4,9,3,6,8,3,4,9,8,11,1,1]
n = len(lst)
print("All sublists: ")
for i in range(n):
    for j in range(i, n+1):
        print(lst[i:j])