from datetime import datetime
from playsound import playsound

play_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

def check_time(play_time):
    if len(play_time) != 11:
        return "Invalid time format! Please try again!"
    else:
        if int(play_time[0:2]) > 12:
            return "Invalid hour! Please try again!"
        elif int(play_time[3:5]) > 59:
            return "Invalid minute! Please try again!"
        elif int(play_time[6:8]) > 59:
            return "Invalid second! Please try again!"
        else:
            return "true"

while True:
    alarm_time = play_time
    validate = check_time(alarm_time.lower())
    if validate != "true":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('alarm.wav')
                    break

