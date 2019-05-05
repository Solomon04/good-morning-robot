import json
import requests

class User:
    def __init__(self):
        try:
            file = open('user.json', 'r')
            data = file.read()
            user = json.loads(data)
            self.name = user['name']
        except FileNotFoundError:
            name = self.get_name()
            api_key = self.get_api_key()
            user_data = {
                'name': name,
                'apiKey': api_key
            }
            data = json.dumps(user_data)
            file = open('user.json', 'w')
            file.write(data)
            self.name = name

    def get_name(self):
        return input("What is your name?\n")

    def get_api_key(self):
        email = input("What is your TODO app email?\n")
        password = input("What is your TODO app password?\n")
        auth = {
            'email': email,
            'password': password
        }
        data = json.dumps(auth)
        url = "http://solomon.todo/api/key"

        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "f5f3f904-41e0-4410-9020-3bafb7063cad"
        }

        response = requests.request("POST", url, data=data, headers=headers)
        if response.status_code != 200:
            print(response.text + "\n")
            print("Try Again.")
            self.get_api_key()
        res = json.loads(response.text)
        return res['api_token']

