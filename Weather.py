import pyowm

class Weather:

    def __init__(self):
        self.owm = pyowm.OWM('c80b8f92532faf48596baba714c9a19a')
        weather = self.get_weather()
        message1 = self.message_one(weather['low'])
        message2 = self.message_two(weather['high'])
        self.message = message1 + " " + message2

    def get_weather(self):
        observation = self.owm.weather_at_place('Burnsville, USA')
        w = observation.get_weather()
        wind = w.get_wind()
        temperature = w.get_temperature('fahrenheit')
        high = temperature['temp_max']
        low = temperature['temp_min']
        return {'high': int(high), 'low': int(low)}

    def message_two(self, high):
        placeholder_two = "and reach a {} high of {} degrees. \n"
        if high < 30:
            return placeholder_two.format("freezing", high)
        elif 31 <= high < 40:
            return placeholder_two.format("cold", high)
        elif 41 <= high < 50:
            return placeholder_two.format("chilly", high)
        elif 50 <= high < 65:
            return placeholder_two.format("cool", high)
        elif 65 <= high < 75:
            return placeholder_two.format("warm", high)
        elif high > 75:
            return placeholder_two.format("hot", high)

    def message_one(self, low):
        placeholder_one = "The weather will start out as a {} {} degrees"
        if low < 30:
            return placeholder_one.format("freezing", low)
        elif 31 <= low < 40:
            return placeholder_one.format("cold", low)
        elif 41 <= low < 50:
            return placeholder_one.format("chilly", low)
        elif 50 <= low < 65:
            return placeholder_one.format("cool", low)
        elif 65 <= low < 75:
            return placeholder_one.format("warm", low)
        elif low > 75:
            return placeholder_one.format("hot", low)

