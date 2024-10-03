def birdcalls():
    global curse
    gl = 'aeiouy'
    text = sorted(curse.split(), key=lambda x: len(x))
    for i in range(0, len(text), 2):
        temp_word = list()
        for j in range(len(text[i])):
            if text[i][j].lower() in gl:
                temp_word.append('*')
            else:
                temp_word.append(text[i][j].upper())
        text[i] = ''.join(temp_word)
    curse = ' '.join(text[:])

curse = "Good! Ah perishing good! Are you afraid now? Afraid?"
birdcalls()
print(curse)
