'''
## TO DO
Did you finish physical setup?
VS Code linked to Github?
Pick an open source project based on welcoming new contributors

Front end for data entry and display?
Who is my user and what problem are they solving?
Python script for testing your own is_prime function using api to check?

Consider separating concerns including todo, imports, configs, helper functions, data initialization
Include json request and response in v2
Include prime factorization in v3
Early users or mentor feedback?

Handle negative numbers
Handle -1, 0, 1
How do I find users?
Host on heroku?
Or is it time to switch to accountability app?

Can I connect to Project Euler community?
That is closer to test cases for each question with varying degrees of difficulty
with feedback on thought process errors? Or recommend next problem to build confidence or acquire next skill?
Setup feedback?
Implement zendesk tickets?

'''

## IMPORTS
from flask import Flask, jsonify, request, render_template

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
This allows for a quick primality check
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

## MAIN
app = Flask(__name__)

# Define the route for checking primality using query parameters
@app.route('/v1/is_prime', methods=['GET'])
def check_prime():
    try:
        # Extract 'number' from the query parameters
        num = int(request.args.get('number'))

        # Check if the number is prime
        result = is_prime(num)
        
        # Return the result as a JSON response
        return jsonify({"number": num, "is_prime": result})

    except (TypeError, ValueError):
        # Or return an error message
        return jsonify({"error": f"Please provide an integer."}), 400

@app.route('/')
@app.route('/v1/')
def home():
    return render_template('home.html', limit=prime_list[-1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
