# # 34. Write a Python program that uses the Sieve of Eratosthenes method to
# # compute prime numbers up to a specified number.
# # Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον
# # Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number
# # sieves, is a simple, ancient algorithm for finding all prime numbers up to any
# # given limit.
# Bắt đầu với danh sách tất cả số được coi là nguyên tố (True).
# 0 và 1 không phải số nguyên tố, nên đánh dấu là False.
# Bắt đầu từ p = 2, đánh dấu tất cả bội số của p là không nguyên tố.
# Lặp lại cho số tiếp theo chưa bị đánh dấu (p) cho đến khi p * p > n.
# Các số còn lại là True chính là các số nguyên tố.

n= int(input("Enter the limit: "))
prime = [True for _ in range(n+1)]
prime[0] = prime[1] = False

p=2
while p*p <= n:
    if prime[p]:
        for i in range(p*p, n+1, p):
            prime[i] = False
    p +=1
print(f"Primes to {n} are: ")
for i in range(n+1):
    if prime[i]:
        print(i, end=" ")