import dejurnue
import raspisanie
import vkmessage
import weather_scraber
import schedule
import datetime
import time
import functools


def main():
    weather = weather_scraber.weather_get("4a744877-13d9-4b02-87cb-d8e148d29708")
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
    today = datetime.datetime.today().isoweekday()
    messages = f'''
    @all \n Доброе утро! \n Сегодня дежурит - {dejurnue.send_names(number_parta)}. \n Сейчас на улице {weather[2]}°C, {weather[3]}. \n Днем будет {weather[0]}°C, {weather[1]} \n Расписание: \n {raspisanie.raspisanie_list[today]} 
'''
    vkmessage.send_utro("3", messages, "")

schedule.every().day.at("06:30").do(main)

def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator

@catch_exceptions(cancel_on_failure=True)
def bad_task():
    return 1 / 0

schedule.every(60).seconds.do(bad_task)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print()

