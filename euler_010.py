"""
Project Euler - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all primes below two million.
"""

def find_primes(max_candidate):
    primes = []
    candidate = 2

    while candidate <= max_candidate:
        trial_divisor = 2
        prime = True

        while trial_divisor * trial_divisor <= candidate:
            if candidate % trial_divisor == 0:
                prime = False
                break
            trial_divisor += 1

        if prime:
            primes.append(candidate)
        candidate += 1
    return primes

print sum(find_primes(2000000))
