import requests
from features import payload
from Utilities.configurations import *

auth_endpoint = getconfig()['API']['endpoint'] + "/auth"

auth_response = requests.post(url=auth_endpoint, json=payload.authpayload(), headers=payload.headers())

auth_response_json = auth_response.json()

assert auth_response.status_code == 200

print(auth_response_json)
print(auth_response_json['token'])
