# 7. Write a Python program to remove duplicates from a list.
lst = ['cnc','cnc','emla','dore','mifa']
new_lst = []
for x in lst:
    if x not in new_lst:
        new_lst.append(x)

print("Original list: ", lst)
print("List after removing duplicates: ", new_lst)
        