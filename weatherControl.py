import requests

URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "9939b09eba922f03e95fbe11bcbda821"


class WeatherControl():
    def __init__(self):
        self.url = URL

    def find_weather_info(self, parameters):
        querystring = {
            'lat': parameters[0],
            'lon': parameters[1],
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.request("GET", self.url, params=querystring)
        res = response.json()
        temp = res['current']['temp']
        hum = res['current']['humidity']
        weather = res['current']['weather'][0]['description']
        params = (temp, hum, weather)
        return params

