import requests
import json
import configparser


class User:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    url = parser.get('CONFIG', 'SERVICE_URL')
    login = parser.get('CONFIG', 'USERNAME')
    password = parser.get('CONFIG', 'PASSWORD')
    auth_req = parser.get('CONFIG', 'MAKE_AUTH')
    req = parser.get('CONFIG', 'GET_REQ')

    @staticmethod
    def make_auth():
        params = {"username": User.login, "password": User.password}
        response = requests.post(url=User.url + User.auth_req, data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return (response.json()).get("access")

    @staticmethod
    def make_req(token, offset):
        head = {'Authorization': 'Bearer {}'.format(token)}
        params = {"limit" : 100, "offset" : offset}
        response = requests.get(url=User.url + User.req,params=params, headers=head, stream=True)
        return response.json()