import dejurnue
import raspisanie
import vkmessage
import weather_scraber
import schedule
import datetime
import time


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
    @all \n Доброе утро! \n Сегодня дежурит - {dejurnue.send_names(number_parta)}. \n Сейчас на улице {weather}°C. Расписание: \n 1.  Английский / Информатика \n 2. Физика \n 3. Математика \n 4. Математика \n 5. Химия 
'''
    today = datetime.datetime.today().isoweekday()
    vkmessage.send_utro("3", messages, "")

schedule.every().day.at("06:30").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
