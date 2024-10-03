text = input()
num = int(input())
temp_text1, temp_text2 = text, text
for _ in range(abs(num)):
    temp_text1 = temp_text1[1:] + temp_text1[:1]
    temp_text2 = temp_text2[-1:] + temp_text2[:-1]
if num < 0:
    temp_text1, temp_text2 = temp_text2, temp_text1
print(temp_text1)
print(text)
print(temp_text2)