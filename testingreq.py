# Posting with Basic Authentication i.e using UserName and Password

import requests, json

API_STARTPOINT = "https://devtest.fueblabs.com/rest/persistence/items"
API_ENDPOINT = "http://127.0.0.1:8000/adddata"

session = requests.Session()
session.auth = ('rajathtest@gmail.com','fueb1')
r = session.get(url=API_STARTPOINT)
# k= r.text
k = r.json()
# print(k)
data = {}
for i in k:
    # print(i)
    data['name'] = i['name']
    data['presentstate'] = True if i['state'] == 'ON' else False
    data['onoffstate'] = True if i['OnOffState'] == 'ON' else False
    data['timestampnow'] = i['timestampNew']
    dataey = json.dumps(data)
    p = requests.post(url=API_ENDPOINT, data=dataey)
    l = p.text
    print(l)
    data = {}
# print(data)


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

# import requests
#
# url = 'http://127.0.0.1:8000/universities/'
# headers = {'Authorization': 'Token 534b79cb082fdd671159aaaa96687dbdee4cbf69'}
# r = requests.get(url, headers=headers)
# print(r.text)
