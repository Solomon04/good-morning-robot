import json
import random

class Quote:

    def __init__(self):
        self.message = self.select_random_quote()

    def select_random_quote(self):
        file = open('quotes.json', encoding="utf8")
        data = file.read()
        dict = json.loads(data)
        int = random.randint(0,101)
        quote = dict['quotes'][int]['quote']
        author = dict['quotes'][int]['author']
        pause = "<break time=\"200ms\"/>"
        message = "Here is the quote of the day:" + pause + quote + pause + "by" + author
        return message

