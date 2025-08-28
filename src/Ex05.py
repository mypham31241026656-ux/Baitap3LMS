# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def ex_04():
    str = ['abc','cbd','apa','upu','ete']
    dem = 0
    for st in str:
        if len(st) < 2:
            print('Len of item is less than 2')
            continue
        if st[0] == st[-1]:
            dem += 1
    print(f"Number of item with the first char and the last char are the same: {dem}")

if __name__ == '__main__':
    ex_04()