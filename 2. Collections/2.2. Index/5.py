text = input()
for letter in text:
	if letter == " ":
		print("\n", end="")
	else:
		print(letter, end="")