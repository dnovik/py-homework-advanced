import requests
import json
from urllib.parse import urlencode


credentials = r'D:\Python\Netology\3.3.classes.vk\credentials.json'

with open(credentials) as f:
    data = json.load(f)
    user_id = data['user_id']
    token = data['TOKEN']

BASE_URL = 'https://api.vk.com/method'


class User:
    
    def __init__(self, token):

        self.token = token

    def get_params(self):
        params = {

        }

    def get_user_id(self):
        pass

    def user(self):
        params = {
            'id' : id
        }
        link = requests.get('').url

        return link


params = {
    'client_id' : '6984152',
    'display' : 'page',
    'scope' : 'friends ',
    'response_type' : 'token',
    'v' : '5.95'
}
token_url = 'https://oauth.vk.com/authorize'

print('?'.join(token_url, urlencode(params)))
