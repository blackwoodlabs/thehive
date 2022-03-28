import sys
import json
import requests

uri = sys.argv[1]
hive_token = sys.argv[2]


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def del_alerts(del_uri):
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    r = requests.delete(del_uri, auth=BearerAuth(hive_token),
                     verify=False, headers=headers)
    print(r.text)

def get_alerts():
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    r = requests.get(uri, auth=BearerAuth(hive_token),
                        verify=False, headers=headers)
    j = json.loads(r.text)
    for i in j:
        del_uri = uri+i['id']
        del_alerts(del_uri)

def run():
    while True:
        get_alerts()

run()
