def palindrome():
    with open('Homework/input.dat', 'rb') as f: 
        lines = f.readlines()

    if lines:
        return [line.strip() for line in lines] == [line[::-1].strip() for line in lines[::-1]] 
    else:
        return True

print(palindrome())