from datetime import datetime, timedelta

users = [
    {"name": "Milentiy", "Birthday": "08 May 1997"},
    {"name": "Alena", "Birthday": "07 September 1987"},
    {"name": "Dmytro", "Birthday": "18 August 1987"},
    {"name": "Milana", "Birthday": "16 December 1987"}
]

weekdays = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
        }

def get_birthdays_per_week(users):
    scurrent_date = datetime.now().date()
    end = scurrent_date + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["Birthday"], "%d %B %Y")
        date_birthday = datetime(scurrent_date.year, birthday.month, birthday.day)
        if scurrent_date <= date_birthday.date() <= end:
            day = date_birthday.weekday()
            if day == 0:
                weekdays['Monday'] += i['name']
                weekdays['Monday'] += ', '
            if day == 1:
                weekdays['Tuesday'] += i['name']
                weekdays['Tuesday'] += ', '
            if day == 2:
                weekdays['Wednesday'] += i['name']
                weekdays['Wednesday'] += ', '
            if day == 3:
                weekdays['Thursday'] += i['name']
                weekdays['Thursday'] += ', '
            if day == 4:
                weekdays['Friday'] += i['name']
                weekdays['Friday'] += ', '
            if day in (5, 6):
                weekdays['Next Monday'] += i['name']
                weekdays['Next Monday'] += ', '

    for a, b in weekdays.items():
        count = 0
        if len(b) > 0:
            print(a + ': ' + b[:-2])
        else:
            count += 1
    if count > 0:
        print("No Birthday in this week. Be happy)")



get_birthdays_per_week(users)