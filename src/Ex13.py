# 13. Write a Python program to generate a 3*4*6 3D array whose each element is
# *.

array = [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
for i in array:
    for j in i:
        print(j)
    print()
