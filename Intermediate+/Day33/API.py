import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)

data = response.json() # Actual data
print(data)

print(data['iss_position']['longitude'])
print(data['iss_position']['latitude'])
