# sieve of Eratosthenes  --->  O(nloglogn)
primes = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):  # O(n)
    if primes[i]:
        for j in range(i * i, n + 1, i): # sum( n/p ) ~ O(loglogn)
            primes[j] = False

# sieve of Euler
primes = []
is_prime = [True] * (n+1)
for i in range(2, n + 1):  # ~ O(n)
    if is_prime[i]:
        primes.append(i)
        
    for p in primes:
        if p * i > n:
            break
        else:
            is_prime[ p * i ] = False
        if i % p == 0:
            break
