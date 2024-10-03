ingr = dict()
coctails = {'Сладкоежка': 'банан, молоко, мороженое', 
            'Клубнично-банановый': 'клубника, молоко, банан, мороженое',
            'Клубничный': 'клубника, молоко, мороженое',
            'Хушаф': 'финики, молоко',
            'Банановый': 'банан, молоко, финики'}
for _ in range(5):
    text = input().split(': ')
    ingr[text[0]] = ingr.get(text[0], 0) + int(text[1])
num = int(input())
for _ in range(num):
    order = input()
    needs = coctails[order].split(', ')
    checker = True
    for item in needs:
        if ingr[item] > 0:
            continue
        else:
            checker = False
            break
    if checker:
        for item in needs:
           ingr[item] -= 1
        print(f'Пожалуйста, ваш {order}. Приятного аппетита!')
    else:
        print('Извините, не можем выполнить заказ.')  