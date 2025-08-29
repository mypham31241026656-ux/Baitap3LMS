# 17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

data = [3, 5, 7, 13]
all_prime = True
for n in data:
    if n<2:
        all_prime = False
        break
    for i in range(2, int(n**0.5)+1): #Tất cả đều có ít nhất một ước ≤ căn bậc 2.
        if n % i == 0:
            all_prime = False
            break
    if not all_prime:
        break
print(all_prime)