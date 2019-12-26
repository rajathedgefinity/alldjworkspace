# Posting with Basic Authentication i.e using UserName and Password

# import requests
#
# API_ENDPOINT = "http://127.0.0.1:8000/universities/"
#
# data = {
#     "name":"vtu"
# }
#
# session = requests.Session()
# session.auth = ('admin','adminpassword')
# r = session.post(url=API_ENDPOINT, data=data)
# k= r.text
# print(k)

# Posting with 2nd Method of Basic Authentication using Username and password_validation

# import requests
# from requests.auth import HTTPBasicAuth
#
# API_ENDPOINT = "http://127.0.0.1:8000/universities/"
#
# data = {
#     "name":"Mysore"
# }
# r = requests.post(url = API_ENDPOINT, data = data, auth=HTTPBasicAuth('admin','adminpassword'))
# k = r.text
# print(k)

# Getting with Authentication key

import requests

url = 'http://127.0.0.1:8000/universities/'
headers = {'Authorization': 'Token 534b79cb082fdd671159aaaa96687dbdee4cbf69'}
r = requests.get(url, headers=headers)
print(r.text)
