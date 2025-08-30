# 35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
#Nối mỗi phần tử của danh sách với các số từ 1 đến n:

sample_list = ['p','q']
n = int(input('Enter n: '))
result = []
for i in range(1,n+1):
    for item in sample_list:
        result.append(f'{item}{i}')
print("Result list: ",result)