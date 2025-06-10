import requests
import time
import uuid

# API endpoint
url = "https://api-ecommerce.essencetechnologies.com/api/customer/register"

# Generate unique username and email to avoid duplicates
unique_id = uuid.uuid4().hex[:8]
username = f"Rupesh{unique_id}"
email = f"rmmahat{unique_id}@gmail.com"

# Request payload
payload = {
    "password": "Sebs@123",
    "confirmPassword": "Sebs@123",
    "username": username,
    "firstName": "Rupesh",
    "lastName": "Mahat",
    "email": email,
    "phoneNo": "9876543210",
    "phoneNo2": "987654321"
}

# Measure response time
start = time.time()
response = requests.post(url, json=payload)
end = time.time()
response_time = (end - start) * 1000  # milliseconds

# Output and debug info
print(f"Status Code: {response.status_code}")
print(f"Response Time: {response_time:.2f} ms")

try:
    response_data = response.json()
    print("Response JSON:", response_data)
except Exception:
    print("Response Text:", response.text)

# Assertions
assert response_time < 1000, "❌ API response time is too slow!"
assert response.status_code == 200, f"❌ API request failed! Status: {response.status_code}"
