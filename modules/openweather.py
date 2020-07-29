import requests
import urllib.parse

api_id = 'da1bf1f33a51a2bfa3ce1745bf65fd7f' # Open Weather Map api key
units = 'metric'

def get_weather(city):
    """
    This function gets the weather from a city using Open Weather Map api.
    """
    print("Getting weather from {}".format(city))
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(urllib.parse.quote(city), units, api_id)
    print(url)
    return requests.get(url).json()