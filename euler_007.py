"""
Project Euler - Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def factor(num):
    l = []
    x = math.floor(math.sqrt(num))
    while x > 1:
        if not num % x:
            l.extend([int(x), int(num/x)])
        x -= 1
    return l

def is_prime(num):
    return not len(factor(num))

primes = []
x = 2
while len(primes) < 10001:
    if is_prime(x):
        primes.append(x)
    x += 1

print primes[10000]
