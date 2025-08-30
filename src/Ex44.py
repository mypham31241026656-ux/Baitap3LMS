# 44. Write a Python program to generate groups of five consecutive numbers in a
# list.
#tạo các nhóm (list con) gồm 5 số liên tiếp.

result = []
for i in range(1,21,5): #chạy từ 1 đến 20, bước nhảy 5
    group = list(range(i,i+5))
    result.append(group)
print("Groups include: ",result)
