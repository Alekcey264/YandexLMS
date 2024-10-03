from datetime import datetime

def days_left(date):
    return (datetime.strptime(date, "%d.%m.%Y") - datetime.today()).days

print(days_left('31.12.2022'))