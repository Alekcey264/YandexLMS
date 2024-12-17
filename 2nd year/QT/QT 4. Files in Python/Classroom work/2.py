change = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",  
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",  
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",  
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",  
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",  
    "б": "b", "ю": "ju", "ё": "jo"
}
with open('Classroom work/cyrillic.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if lines:
        for line in lines:
            text = ''
            for letter in line.strip():
                if letter.lower() in change.keys():
                    if letter.isupper():
                        text += change[letter.lower()].capitalize()
                    else:
                        text += change[letter]
                else:
                    text += letter
            with open('Classroom work/transliteration.txt', 'a', encoding='utf-8') as f:
                f.write(text + "\n")