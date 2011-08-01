"""
Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600 851 475 143 ?
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

TEST_NUM = 600851475143
factors = factor(TEST_NUM)
factors.sort()
factors.reverse()

for x in factors:
    if is_prime(x):
        print "Largest prime factor of %s is %s." % (TEST_NUM, x)
        break
