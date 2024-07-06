from datetime import date, timedelta
 
y, m, d = map(int, input().split('/'))
 
start_date = date(y, m, d)
present = int(input())
days = int(input())
 
start_date += timedelta(100 // present)
 
while days > 0:
    if start_date.weekday() < 5:
        print(start_date.strftime('%a %d %b'))
        days -= 1
    start_date += timedelta(1)