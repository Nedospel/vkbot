import dejurnue
import raspisanie
import vkmessage
import weather_scraber
import schedule
import datetime

def main():
    f = open('number_parta.txt', 'r+')
    number_parta = int(f.read())
    f.seek(0)
    if str(number_parta) == "15":
        f.truncate()
        f.write("1")
        f.close()
    else:
        f.write(str(number_parta + 1))
        f.close()
    weather = weather_scraber.weather_get("722cc1d8-68fb-4460-b269-9248a671a22d")
    messages = f'''
    @all \n Доброе утро! Сегодня дежурит - {dejurnue.send_names(number_parta)}. Сейчас на улице {weather}°C. Расписание: 
'''
    today = datetime.datetime.today().isoweekday()
    vkmessage.send_utro("1", messages, "photo-204420308_457239022")
main()
