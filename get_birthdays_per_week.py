from datetime import datetime
from collections import defaultdict 
def get_birthdays_per_week (users):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    users_birthday = defaultdict(list)
    today =  datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()
            if day_of_week == 5 or day_of_week == 6:
                users_birthday[0].append(name)
            else:
                users_birthday[day_of_week].append(name)

    for k,v in users_birthday.items():
            print(f"{days[k]}: {', '.join(map(str, v))}")

    