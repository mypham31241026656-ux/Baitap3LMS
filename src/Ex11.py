# 11. Write a Python function that takes two lists and returns True if they have at
# least one common member
#Kieemr tra trong 2 list co it nhat 1 phan tu chung

list1 = [1,4,7,9]
list2 = [2,4,7,10]

found = False
for x in list1:
    if x in list2:
        found = True
print("common member is:", found)