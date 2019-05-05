from Todo import Todo
from Weather import Weather
from News import News
from Greeting import Greeting
from Audio import Audio
from playsound import playsound
from User import User
from Quote import Quote

# Get User
user = User()
name = user.name

# Message from Greeting
greeting = Greeting(name)
greeting_message = greeting.message + "\n"

brief_pause = "<break time=\"300ms\"/>"
pause = "<break time=\"1000ms\"/>"
# print(greeting_message)

# Message from todoClass
todo = Todo()
todo_message = todo.message+ "\n"
# print(todo_message)

# Message from weather class
weather = Weather()
weather_message = weather.message + "\n"
# print(weather_message)

# Message from News class
news = News()
news_message = news.message+ "\n"

# Message from Quote Class
quote = Quote()
quote_message = quote.message


close_message = user.name + brief_pause + "is there anything I can help you with?"
message = "<speak>" + greeting_message + brief_pause + todo_message + pause + weather_message + pause + news_message + brief_pause + quote_message + brief_pause + close_message + "</speak>"

audio = Audio(message)
playsound(audio.audio)