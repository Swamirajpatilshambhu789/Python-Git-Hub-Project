import requests

limit = 1
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'rcQCPRDdYMUZM88WTYUMVg==iJACOh0etertCVPl'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)