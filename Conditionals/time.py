import datetime
now = datetime.datetime.now().hour
print(now)
if now <= 12:
    print("good morning")
elif now <= 18:
    print("good afternoon")
elif now <= 22:
    print("good evening")
else: 
    print("go to bed")