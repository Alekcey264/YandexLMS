text = input().split(", ")
names = ["flower", "gemstone"]
text = "; ".join([names[i % 2] for i in range(len(text))])
print(text)