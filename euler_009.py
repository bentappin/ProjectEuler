"""
Project Euler - Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for x in range(1, 1001):
    for y in range(x+1, 1001):
        a = y*y - x*x
        b = 2 * x * y
        c = x*x + y*y
        if a+b+c == 1000:
            print a*b*c
            break
