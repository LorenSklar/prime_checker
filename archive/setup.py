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
