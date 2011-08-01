"""
Project Euler - Problem 4

A palendromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def is_palendromic(num):
    num = str(num)
    return num == num[::-1]

def factor(num):
    l = []
    x = math.floor(math.sqrt(num))
    while x > 1:
        if not num % x:
            l.extend([int(x), int(num/x)])
        x -= 1
    return l

counter = 999 * 999
x = y = largest_p = None

while counter > 1:
    if is_palendromic(counter):
        factors = factor(counter)
        if factors and len(str(factors[0])) == 3 and len(str(factors[1])) == 3:
            largest_p = counter
            x = factors[0]
            y = factors[1]
            break
    counter -= 1

print "%s x %s = %s" % (x, y, largest_p)
