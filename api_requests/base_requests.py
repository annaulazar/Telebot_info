import requests

from config import config


def get_city_coord(city: str) -> str:
    payload = {'geocode': city, 'apikey': config.apis.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    return r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']


def get_weather(city):
    coordinates = get_city_coord(city).split()
    payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
    headers = {'X-Yandex-API-Key': config.apis.weather_key}
    r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers=headers)
    weather_data = r.json()
    return weather_data['fact']


print(get_weather('Новокузнецк'))
