counter = 1
string = input()
while not string.isupper():
    if string[:9] == "отпечаток":
        break
    if counter == 1:
        print(string.upper())
        counter += 1
    elif counter == 2:
        print(string.title())
        counter += 1
    elif counter == 3:
        print(string.lower())
        counter += 1
    else:
        print(string.capitalize())
        counter = 1
    string = input()