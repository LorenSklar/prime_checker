import sympy

num = 2 ** 3217 - 1
result = sympy.isprime(num)
print(num, "is prime." if result else "is not prime.")
