times = list()
text = input()
while text:
    text = text.split()
    nums = list(map(int, text[1].split(':')))
    times.append((text[0], nums[0] * 3600 + nums[1] * 60))
    text = input()
current_time = list(map(int, input().split(':')))
current_time = current_time[0] * 3600 + current_time[1] * 60
paths = input().split()
closest = 24 * 3600
for item in paths:
    for time in times:
        if time[0] == item and time[1] > current_time:
            temp = time[1] - current_time - 360
            if temp >= 0 and temp < closest:
                closest = temp
if closest == 24 * 3600:
    print(None)
else:
    print(closest // 60)