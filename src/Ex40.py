# # 40. Write a Python program to split a list based on the first character of a word.
# Input : ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
# Output: {
#     'a': ['apple', 'apricot', 'avocado'],
#     'b': ['banana', 'blueberry'],
#     'c': ['cherry']
# }

words = {'apple','banana','apricot','cherry','blueberry'}
result = {}
for word in words:
    first_char = word[0]
    if first_char not in result:
        result[first_char] = []
    result[first_char].append(word)

print(result)