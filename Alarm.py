from datetime import datetime
# from playsound import playsound   (commented because song not downloaded in office laptop)

def alarm():
    alarm_time = input("Enter the alarm time in 24 hrs HH:MM format : ")
    print(alarm_time)
    current_date_time = datetime.now()
    current_time = current_date_time.strftime("%H:%M")
    print(current_time)
    while alarm_time == current_time:
        print("Levvu ra MABBU!!")
        # playsound("alarm song") commented because song not downloaded in office laptop
        break
alarm()

