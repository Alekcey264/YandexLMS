new_dict = dict()


def diversity(text):
    new_dict[text] = new_dict.get(text, 0) + 1
    return new_dict[text]
