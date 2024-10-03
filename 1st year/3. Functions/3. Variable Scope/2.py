last_calls = []


def prompter(text):
    for item in last_calls:
        if text in item:
            return item
    else:
        last_calls.append(text)
        return text
    