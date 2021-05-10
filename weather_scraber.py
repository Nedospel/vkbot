import requests
import json
def weather_get(yandexweather_api):
    respons = requests.get(
        'https://api.weather.yandex.ru/v2/informers?lat=54.444068&lon=61.276879&[lang=ru_RU]',
        headers={'X-Yandex-API-Key': yandexweather_api},
    )
    responsea = json.loads(respons.text)
    fact = responsea["fact"]
    fact_temp = fact['temp']
    fact_feelslike = fact["feels_like"]
    return fact_temp