from datetime import datetime
hour = datetime.now().hour

earlyMorningHour = '3'
lateMorningHour = '11'

earlyAfternoonHour = '11'
lateAfternoonHour = '16'

now = datetime.now().hour

if int(earlyMorningHour) <= now and int(lateMorningHour) > now:
    print("Good morning!")
elif int(earlyAfternoonHour) <= now and int(lateAfternoonHour) > now:
    print("Good afternoon!")
elif int(earlyAfternoonHour) <= now and int(lateAfternoonHour) > now:
    print("Good evening!")