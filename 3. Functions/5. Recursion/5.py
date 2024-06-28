def happy_number(num):
    if type(num) == int:
        num = list(str(num))
    left_side = int(num.pop(0))
    right_side = int(num.pop())
    if not num:
        return [left_side, right_side]
    left_part, right_part = happy_number(num)
    return [left_side + left_part, right_side + right_part]

print(happy_number(96251231254621))
