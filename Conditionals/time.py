from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

if (11, 30, 0, 0) < now and now >= (4, 0, 0, 0, 0):
    print("Good morning!")
elif (11, 30, 0, 0) > now < (16, 0, 0, 0, 0)
    print("good afternoon")