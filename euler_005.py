"""
Project Euler - Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers form 1 to 20?
"""

# This works but I don't think it's the solution that was had in mind.
# Takes about 2.5 minutes to run on my machine, which would have taken a
# lot longer on a machine from a decade a go (when the problem was set).

import sys
import math

divisors = range(3,20)
x = 2520

while x < sys.maxint:
    all = True
    for d in divisors:
        if x % d:
            all = False
            break
    if all:
        print x
        break
    x += 1
