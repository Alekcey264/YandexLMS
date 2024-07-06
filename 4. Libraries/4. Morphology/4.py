import pymorphy3

def participle(word_in, **grams):
    morph = pymorphy3.MorphAnalyzer()
    values = {value for _, value in grams.items()}
    values.add('PRTF')
    return morph.parse(word_in)[0].inflect(values).word


grammems = {
    'gender': 'femn',
    'number': 'sing',
    'tens': 'pres',
    'case': 'datv'
}
print(participle("плавало", **grammems))