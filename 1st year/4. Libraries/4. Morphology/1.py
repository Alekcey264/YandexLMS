from pymorphy2 import MorphAnalyzer


def russian_noun(text, case="nomn", number="sing"):
    morph = MorphAnalyzer()
    res = morph.parse(text)[1].inflect({case, number}).word
    return res


for case in ["nomn", "gent", "datv", "accs", "ablt", "loct"]:
    print(russian_noun("свечечки", case=case))