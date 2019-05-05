from datetime import datetime

class Greeting:

    # todo change Solomon to be the user from the user data json file.
    def __init__(self, name):
        date = datetime.today().strftime('%m-%d-%Y')
        self.message = "<emphasis level=\"strong\">Good morning" + name + "! Today is " + date + ".\n" + "</emphasis>"
