def mountains(*args, **kwargs):
    second_longer = kwargs.get('second_longer', 0)
    first_smaller = kwargs.get('first_smaller', None)
    common_letters = kwargs.get('common_letters', None)
    presence = kwargs.get('presence', None)

    temp_list = []

    for item in args:
        if second_longer and len(item[1]) - len(item[0]) < second_longer:
            continue
        if first_smaller is not None:
            if first_smaller:
                if item[0][0].lower() >= item[1][-1].lower():
                    continue
            else:
                if item[0][0].lower() < item[1][-1].lower():
                    continue
        if common_letters is not None:
            if len(set(item[0]) & set(item[1])) > common_letters:
                continue
        if presence and presence not in item[1]:
            continue
        temp_list.append((item[0], item[1]))

    if not temp_list:
        return ["", 0]

    max_lex_first = max(item[0] for item in temp_list)
    total_length_second = sum(len(item[1]) for item in temp_list)

    return [max_lex_first, total_length_second]


data = [('Paraguay', 'Uruguay'), ('Gapura', 'Tapajos'), ('Shingu', 'Ucayali'), ('Apure', 'Putumayo')]
conditions = {'second_longer': 1, 'first_smaller': True, 'common_letters': 8, 'presence': 'a'}
print(*mountains(*data, **conditions))