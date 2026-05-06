"""
This file demonstrates how to use the Porsche Dealer API from Python scripts.
"""

import requests
import json

API_BASE_URL = "http://localhost:8000/api"

# Example 1: Login
print("=" * 50)
print("Example 1: Login")
print("=" * 50)

login_data = {
    "email": "dealer@porsche-dealer.com",
    "password": "Dealer@123",
    "dealership_code": "PS-2024",
    "verification_code": "123456"
}

response = requests.post(
    f"{API_BASE_URL}/auth/login/",
    json=login_data
)

print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

if response.status_code == 200:
    user_info = response.json()['user']
    print(f"\n✓ Login successful for: {user_info['email']}")
    print(f"  Dealership: {user_info['dealer_profile']['dealership_name']}")
    
    # Example 2: Get current user info
    print("\n" + "=" * 50)
    print("Example 2: Get Current User")
    print("=" * 50)
    
    headers = {
        'Cookie': response.cookies.get_dict()
    }
    
    user_response = requests.get(
        f"{API_BASE_URL}/auth/user/",
        headers=headers
    )
    
    print(f"Status Code: {user_response.status_code}")
    print(f"Response: {json.dumps(user_response.json(), indent=2)}")
    
    # Example 3: Logout
    print("\n" + "=" * 50)
    print("Example 3: Logout")
    print("=" * 50)
    
    logout_response = requests.post(
        f"{API_BASE_URL}/auth/logout/",
        headers=headers
    )
    
    print(f"Status Code: {logout_response.status_code}")
    print(f"Response: {json.dumps(logout_response.json(), indent=2)}")
else:
    print(f"\n✗ Login failed: {response.json()}")

# Example 4: Invalid credentials
print("\n" + "=" * 50)
print("Example 4: Invalid Credentials")
print("=" * 50)

invalid_data = {
    "email": "invalid@email.com",
    "password": "wrongpassword",
    "dealership_code": "INVALID",
    "verification_code": "123456"
}

invalid_response = requests.post(
    f"{API_BASE_URL}/auth/login/",
    json=invalid_data
)

print(f"Status Code: {invalid_response.status_code}")
print(f"Response: {json.dumps(invalid_response.json(), indent=2)}")
