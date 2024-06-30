gnomes = set()

def real_gnome(text: str):
    if 'gnome' in text.lower():
        if text in gnomes:
            return 'A real gnome, confirmed!'
        else:
            gnomes.add(text)
            return 'The gnome might be real.'
    else:
        return 'No gnome.'

data = ("Why, it's a dwarf!", 'A real gnome!', 'They live in the forest.', 'A real gnome!')
for item in data:
    print(real_gnome(item))