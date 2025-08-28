# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
#Tim cac tu co do dai lon hon n trong mot danh sach tu cho truoc
words = ['apple','banana','cherry','ki']
n=3

result = []
for x in words:
    if len(x) > n: #Neu do dai lon hon n
        result.append(x) #Them tu do vao danh sach
print('Words is longer than',n,":", result)