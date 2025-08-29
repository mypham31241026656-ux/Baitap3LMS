# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
#C1
list = ['Red','Green','White','Black','Pink','Yellow']
for i in [5, 4, 0]: #luôn xóa từ chỉ số lớn → nhỏ để tránh làm lệch vị trí của các phần tử còn lại.
    list.pop(i)
print(f"Expected output is: {list}")
#C2
list = ['Red','Green','White','Black','Pink','Yellow']
result = [list [i] for i in range(len(list))if i not in [0,4,5]]
print("Cách 2: ", end=" ")
print(f"Expected output is: {result}")

#C3
list = ['Red','Green','White','Black','Pink','Yellow']
result = []
for i in range(len(list)):
    if i not in [0,4,5]:
        result.append(list[i])
print(f"Expected output is: {result}")