# 16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both
# included).
#Tạo danh sách các số chính phương (square numbers) từ 1 đến 30 (bao gồm cả 1 và 30).
# In ra 5 phần tử đầu và 5 phần tử cuối của danh sách đó.
square = []
for i in range (1,31):
    if i**2 <= 30:
        square.append(i**2)
print(square)
print("First 5 elements: ", square[:5])
print("Last 5 elements: ", square[-5:])