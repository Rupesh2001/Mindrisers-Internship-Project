import requests
import time

# Sample Swagger API endpoint (e.g., from petstore.swagger.io)
url = "https://api-ecommerce.essencetechnologies.com/api/auth/login"

# Measure response time
start = time.time()
response = requests.get(url)
response = requests.post(url, json={"username": "#", "password": "#"})
end = time.time()

response_time = (end - start) * 1000  # in milliseconds

# Output
print(f"Status Code: {response.status_code}")
print(f"Response Time: {response_time:.2f} ms")

# Assert for maximum allowed response time
assert response_time < 1000, "API response time is too slow!"

# Assert for successful response
assert response.status_code == 200, "API request failed!"
# Assert for expected response content
expected_content = {"message": "Login successful"}
# Print the response content
#print("Response Content:", response.json())
# Print the response headers
print("Response Headers:", response.headers)
