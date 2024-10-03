import pymorphy3
import sys


text = list(map(str.strip, sys.stdin))
morph = pymorphy3.MorphAnalyzer()
p_verbs = set()
imp_verbs = set()
for item in text:
    item = item.replace(',', ' ').replace('?', ' ').replace('!', ' ').replace('.', ' ')
    item = item.replace(':', ' ').split(" ")
    for word in item:
        word = morph.parse(word)
        verb = None
        for part in word:
            if 'VERB' in part.tag or 'INFN' in part.tag:
                verb = part
                break
        if verb:
            if 'perf' in verb.tag:
                p_verbs.add(verb.normal_form)
            elif 'impf' in verb.tag:
                imp_verbs.add(verb.normal_form)
print(*sorted(list(imp_verbs)), sep="\n")  
print(*sorted(list(p_verbs)), sep="\n")