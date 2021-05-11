import requests
import json
conditions = {
"clear" : "ясно",
"partly-cloudy" : "малооблачно",
"cloudy" : "облачно с прояснениями",
"overcast" : "пасмурно",
"drizzle" : "морось",
"light-rain" : "небольшой дождь",
"rain" : "дождь",
"moderate-rain" : "умеренно сильный дождь",
"heavy-rain" : "сильный дождь",
"continuous-heavy-rain" : "длительный сильный дождь",
"showers" : "ливень",
"wet-snow" : "дождь со снегом",
"light-snow" : "небольшой снег",
"snow" : "снег",
"snow-showers" : "снегопад",
"hail" : "град",
"thunderstorm" : "гроза",
"thunderstorm-with-rain" : "дождь с грозой",
"thunderstorm-with-hail" : "гроза с градом"
}
                                            #conditions нужен чтобы менять clear на ясно.
                                            # чтобы нормально выводить условия погоды
def weather_get(yandexweather_api):
    responsea = json.loads((requests.get(
        'https://api.weather.yandex.ru/v2/informers?lat=54.444068&lon=61.276879&[lang=ru_RU]',
        headers={'X-Yandex-API-Key': yandexweather_api}
    )).text)
                                                              #запрос к яндексу. получаю погоду
    fact = responsea["fact"]
    fact_temp = fact["temp"]
    fact_uslovia = conditions[fact["condition"]]
    for i in ((responsea["forecast"])["parts"]):
        if i["part_name"] == "day":
            forecast_day = i
    forecast_day_temp = forecast_day["temp_avg"]
    forecast_day_uslovia = conditions[forecast_day["condition"]]
    return forecast_day_temp, forecast_day_uslovia, fact_temp, fact_uslovia

