text = input()
num = int(input())
if num > 100:
    text = text.replace("0000", "|||")
else:
    for _ in range(3):
        if "|||" in text:
            text = text[:text.index("|||")] + "00" + text[text.index("|||") + 3:]
if "|0|" in text:
    text = text[:text.index("|0|")] + "|00|" + text[text.index("|0|") + 3:]
print(text)
