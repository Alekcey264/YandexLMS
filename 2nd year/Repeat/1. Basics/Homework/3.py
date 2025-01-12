hours = input().split()
minutes = input().split()
for i in range(len(minutes)):
    if len(minutes[i]) < 2:
        minutes[i] = "0" + minutes[i] 
for i in range(len(hours)):
    if len(hours[i]) < 2:
        hours[i] = "0" + hours[i]
hours.sort()
minutes.sort()
for hour in hours:
    sum_of_hours = sum(list(map(int, list(hour))))
    for minute in minutes:
        sum_of_minutes = sum(list(map(int, list(minute))))
        if sum_of_hours != sum_of_minutes:
            print(f"{hour}:{minute}")
