import requests
import json

# Your Fingerprint Secret API Key (replace with your actual secret key)
API_KEY = 'FtINK3IGImpsRaB7Fiyu'

# URL for the Fingerprint Server API (use the appropriate region if needed)
FINGERPRINT_API_URL = 'https://api.fpjs.io/events/'

def get_fingerprint_data(request_id):
    headers = {
        'Auth-API-Key': API_KEY,
        'accept': 'application/json',
    }
    
    # Make a request to the Fingerprint Server API with the given request ID
    response = requests.get(f'{FINGERPRINT_API_URL}{request_id}', headers=headers)
    
    # Check if the response was successful
    if response.status_code == 200:
        return response.json()  # Returns the response data as JSON
    else:
        return {'error': f'Error {response.status_code}: {response.text}'}

# Example usage
request_id = 'your-request-id-here'  # This would be the request ID you get from the frontend
fingerprint_data = get_fingerprint_data(request_id)
print(fingerprint_data)


