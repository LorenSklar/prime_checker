'''
## TO DO
Did you test?
Consider separating concerns including imports, configs, helper functions, data initialization
Include json request and response in v2
Include prime factorization in v3
How do I find users?
Setup feedback?
Implement zendesk tickets?
Or is it time to switch to accountability app?

'''

## IMPORTS
from flask import Flask, jsonify, request, render_template
from random import randint

## CONFIGURATION
limit = 10**6

## FUNCTIONS
def confirm_prime(num):
    """Check if number is prime using trial division for independent confirmation."""
    if num <= 1:
        return False
    
    stop = int(pow(num, 1/2))
    for i in range(2, stop + 1):
        if num % i == 0:
            return False
    return True

def is_prime_up_to_limit(num):
    """Check primality for numbers <= limit using quick compare with least prime factor."""
    return num == least_prime_factors[num]
    
def is_prime_up_to_extended_limit(num):
    """Check primality for numbers <= limit^2 using known primes."""
    stop = int(pow(num, 1/2))
    for prime in prime_list:
        if num % prime == 0:
            return False
        if prime > stop:
            break
    return True

def is_prime_with_no_limit(num):
    """Check primality for numbers > limit^2 returning none if no definitive result."""
    for prime in prime_list:
        if num % prime == 0:
            return False
    return None
    
def is_prime(num):
    if num <= 1:
        return False
    elif num <= limit:
        return is_prime_up_to_limit(num)
    elif num <= limit * limit:
        return is_prime_up_to_extended_limit(num)
    else:
        return is_prime_with_no_limit(num)

## SETUP
'''
This primality check works a little differently. 
Rather than store a boolean
the code stores the least prime factor for each integer up to the limit.
This allows for a primality check
as well as supporting efficient prime factorization.
'''

# initialize list to remember least prime factor
least_prime_factors = [None] * (limit + 1)

# initialize list to hold primes
prime_list = []

# remember least prime factor
for i in range(2, limit + 1):
    if least_prime_factors[i] == None:
        prime_list.append(i)
        for j in range(i, limit + 1, i):
            if least_prime_factors[j] == None:
                least_prime_factors[j] = i

## TEST
ok = True
tests = 10**3
bound = 10**12
for test in range(tests):
    num = randint(-bound, bound)
    slow_check = confirm_prime(num)
    quick_check = is_prime(num)

    if slow_check or quick_check:
        print(num, slow_check, quick_check)
    
    if slow_check != quick_check:
        ok = False
        print(num, slow_check, quick_check)

if ok:
    print(f"Rockstar!")
                
