import requests
import json

class Todo:

    def __init__(self):
        stats = self.get_stats()
        todo = self.get_todo()
        self.message = self.create_message(todo, stats)

    def get_stats(self):
        url = "http://solomon.todo/api/stats"

        payload = ""
        headers = {
            'Authorization': "oPbewlvmzmBuQGbhvZ67sZ8TscFeQLyx7Jdln1eXgIkbmMdc7bcc2ZUbMN64",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "a45f1d47-9ae2-4c29-90cd-62d456abe7d6"
        }

        response = requests.request("GET", url, data=payload, headers=headers)

        return json.loads(response.text)

    def get_todo(self):
        url = "http://solomon.todo/api/today"

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'Authorization': "oPbewlvmzmBuQGbhvZ67sZ8TscFeQLyx7Jdln1eXgIkbmMdc7bcc2ZUbMN64",
            'cache-control': "no-cache",
            'Postman-Token': "8c0fdb3e-fc0a-4dab-8c34-fd1a1dad99f1"
        }

        response = requests.request("GET", url, data=payload, headers=headers)

        return json.loads(response.text)

    def create_message(self, todo, stats):
        placeholder = "You have {} tasks due today. "
        placeholder2 = "Note <break time=\"300ms\"/>, you completed {} of your tasks yesterday. "
        placeholder3 = "<emphasis level=\"strong\">That is a {} job Solomon. {}</emphasis>"
        success_rate = int(round(float(stats['stats']['success_rate'].strip('%'))))
        message1 = placeholder.format(todo['count'])
        message2 = placeholder2.format(str(success_rate) + "%")
        if success_rate < 60:
            message3 = placeholder3.format('terrible', 'Do better!\n')
        elif 61 <= success_rate < 75:
            message3 = placeholder3.format('mediocre', 'Do better!\n')
        elif 75 <= success_rate < 85:
            message3 = placeholder3.format('good', 'Keep it up!\n')
        elif 85 <= success_rate < 99:
            message3 = placeholder3.format('great', 'Keep it up!\n')
        elif success_rate == 100:
            message3 = placeholder3.format('excellent', 'Keep it up!\n')

        return message1 + message2 + message3

