import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.post('http://httpbin.org/post',
                         headers=headers,
                         params={'a': 'b'},
                         json={'username': 'bird'},
                         )

print(response.text)