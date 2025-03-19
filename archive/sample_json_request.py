import json, requests

def prime_check(number):
    url = 'http://127.0.0.1:5010/v2/is_prime'
    headers = {"Content-Type": "application/json"}
    data = {'number': number}
    
    response = requests.get(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Example usage
prime_check(60)
prime_check(-1)
prime_check('abc')
