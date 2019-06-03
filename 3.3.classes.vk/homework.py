import requests
import json


credentials = r'D:\Python\Netology\3.3.classes.vk\credentials.json'

with open(credentials) as f:
    data = json.load(f)
    user_id = data['user_id']
    token = data['access_token']
    client_id = data['client_id']


class User:
    
    def __init__(self, token, user_id, client_id):

        self.user_id = user_id
        self.token = token
        self.client_id = client_id



    def authorization():
        
        URL = 'https://oauth.vk.com/authorize'

        params = {
            'client_id' : client_id,
            'display' : 'page',
            'scope' : 'friends',
            'response_type' : 'token',
            'v' : '5.95'
        }

        response = requests.get(URL, params)

        return response.url


    def get_info():

        URL = 'https://api.vk.com/method/users.get'

        params = {
            'user_ids' : user_id,
            'access_token' : token,
            'fields' : ['id', 'first_name', 'last_name'],
            'v' : '5.95'
        }

        response = requests.get(URL, params).json()

        return response



    def get_mutual_friends(user1, user2):

        URL = 'https://api.vk.com/method/friends.getMutual'

        params = {
            'source_uid' : user1,
            'target_uid' : user2,
            'v' : '5.95'
        }

        response = requests.get(URL, params)

        return response




    def get_friends():

        URL = 'https://api.vk.com/method/friends.get'


        params = {
            'user_ids' : user_id,
            'access_token' : token,
            'v' : '5.95',
            'order' : 'hints',
            'fields' : 'nickname',
            'name_case' : 'nom'
        }

        response = requests.get(URL, params)

        return response.text


User.get_info()