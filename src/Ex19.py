# 19. Write a Python program to calculate the difference between the two lists.
lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7]

diff1 = list(set(lst1) - set(lst2))
diff2 = list(set(lst2) - set(lst1))
print("Có trong list1 nhưng khôgn có trong list2", diff1)
print("Có trong list2 nhưng khôgn có trong list1", diff2)