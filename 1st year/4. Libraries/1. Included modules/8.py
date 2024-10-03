from datetime import datetime, date
 
 
def asteroid_angle(n):
    data1 = date.today()
    data2 = date(2000, 1, 1)
    if data1 != date.today():
        data1 = datetime.strptime(data1, '%Y-%m-%d')
        gravity = round(360 / n * ((data1 - data2).days % n))
    else:
        gravity = round(360 / n * ((data1 - data2).days % n))
    return gravity

print(asteroid_angle(220))