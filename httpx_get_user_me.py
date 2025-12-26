import httpx


payload = {
    'email': 'usertest@example.com',
    'password': '12345'
}

response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload)
response_data = response.json()

users_me_headers = {
    'Authorization': f'Bearer {response_data["token"]["accessToken"]}'
}

users_me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=users_me_headers)
users_me_response_data = users_me_response.json()

print(users_me_response_data)
print(users_me_response.status_code)
