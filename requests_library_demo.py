import requests
from getpass import getpass
from requests.exceptions import Timeout

#GET Request Example
response = requests.get('https://api.github.com')

print(response)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

print(response.json())

#POST Request Example
payload = {'name': 'EE461L', 'mascot': 'nemo'}
postrequest = requests.post('https://httpbin.org/post', data=payload)

pr_dict = postrequest.json()
print(pr_dict['form'])
print(postrequest.text)

#Authentication Example
request = requests.get('https://api.github.com/user', auth=('<YOUR GITHUB USERNAME>', getpass()))
print(request)

#Timeout Example

r = requests.get('https://api.github.com', timeout=.1)
#r = requests.get('https://api.github.com', timeout=.0004)
print(r)

try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')