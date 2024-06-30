def circle_tail(*arr, **additional_commands):
    arr = list(arr)
    if 'shift' in additional_commands:
        for i in range(len(arr)):
            arr[i] = arr[i][additional_commands['shift']:] + arr[i][:additional_commands['shift']]
    special = []
    for item in arr:  
        word = set()
        temp_data = item.split('##')
        for letter in temp_data[0]:
            if letter not in temp_data[1] and letter != ' ' and letter != '.':
                word.add(letter)
        word = list(word)
        if 'in_order' in additional_commands:
            if additional_commands['in_order']:
                word = sorted(word)
            else:
                word = sorted(word, reverse=True)
        special.append((len(temp_data[0].split()) + len(temp_data[1].split()), ''.join(word)))
    if 'in_order' in additional_commands:
        if additional_commands['in_order']:
            return sorted(special, key=lambda x: (x[0], x[1]))
        else:
            return sorted(special, key=lambda x: (-x[0], -x[1]))
    return special
    

data = ['This Fox does not even seem to think##I am human', 'Nils thought##pulled the Foxs tail as hard as he could', 'In surprise Smirre released the goose.##Just for a second.']
#print(*circle_tail(*data), sep="\n")
data = ['And Smirre tried to grab Nils##But it was not so easy', 'Nils held on to its tail##with both hands', 'Smirre jumped to the right##and the tail turned to the left', 'Smirre leaped to the left##and the tail turned to the right']
print(*circle_tail(*data, in_order=True, shift=5), sep="\n")