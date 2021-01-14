url = 'https://reqres.in/api/users?page=2'

""" use GET api call to fetch the data, make sure it is in json format and not text format,
    users list is present with key name 'data', print each user full name(first_name last_name)"""

import requests
import json

res = requests.get(url)
data = res.json()
print(type(data))
# print(data.get('data')[0])
# for user in data.get('data'):
#     print(user.get('first_name'), user.get('last_name'))
    
