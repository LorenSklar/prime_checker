## INITIALIZATION
from flask import Flask, jsonify, request, render_template
from sympy import isprime

## HELPER FUNCTIONS 
def is_prime(num):
    if num <= 1:
        return False
    else:
        return isprime(num)

## MAIN         
app = Flask(__name__)

# Define the route for checking primality using query parameters
@app.route('/v2/is_prime', methods=['GET', 'POST'])
def check_prime():
    try:
        # Extract 'number' from the query parameters
        num = request.json.post('number')

        # Check if the number is prime
        result = is_prime(num)
        
        # Return the result as a JSON response
        return jsonify({"number": num, "is_prime": result})

    except (TypeError, ValueError):
        # Or return an error message
        return jsonify({"error": f"Please provide an integer."}), 400

@app.route('/')
@app.route('/v2/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
