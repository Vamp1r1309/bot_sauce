
def check_value():
    dic = {
        'Сырный ': '',
        'сырный ': '',
        'Томат ': '',
        'томат ': '',
        'Чесночный ': '',
        'чесночный ': '',
        'Пикантный ': '',
        'пикантный ': '',
        'Хрен ': '',
        'хрен ': '',
        'Грибной ': '',
        'грибной ': ''
    }

    for i in dic.keys():
        dic[i] = [i for i in range(1, 1800)]
    lis = []
    key_lis = []
    for k, v in dic.items():
        lis.append(str(v).split())
        key_lis.append(k)
    res_lis = []
    for i in key_lis:
        for j in lis:
            temp = ''
            for k in j:
                temp += i + k.replace(']', '').replace('[', '')
        res_lis.append(temp)
    tmp = set(res_lis)
    st = str(res_lis).replace('[', '').replace(']', '').replace("'", "").split(',')
    st1 = str(set(res_lis)).replace('[', '').replace(']', '').replace("'", "").replace(' ', '').split(',')
    return st + st1


#---------------------------------------------------------------------------------------------------------------------------------------
def check_value_state(message):
    from math import ceil
    lis = message.split()
    message, num = lis[0], lis[1]
    if 'сырный' in message.lower():
        return f"Сметана - {int(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.2)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Сырный ар. - {format(int(num) * 0.13 / 162, '.2f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n" + \
        f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n"
    elif 'грибной' in message.lower():
        return f"Сметана - {int(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.2)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Лук - {format(int(num) * 0.13 / 40, '.2f')} кг.\n" + f"Грибы - {format(int(num) * 0.13 / 70, '.2f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 880, '.3f')} кг.\n" + \
        f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n"
    elif 'пикантный' in message.lower():
        return f"Сметана - {int(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.2)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Лук - {format(int(num) * 0.13 / 14, '.2f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n" + \
                f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n"

    elif 'чесночный' in message.lower():
         return f"Сметана - {int(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.2)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Чеснок - {format(int(num) * 0.13 / 80, '.2f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 624, '.3f')} кг.\n" + f"Красный перец - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n" + \
f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n"
    elif 'хрен' in message.lower():
        return f"Сметана - {int(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.2)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Хрен - {format(int(num) * 0.13 / 90, '.2f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 624, '.3f')} кг.\n" + f"Красный перец - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n" + \
f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n"
    elif 'томат' in message.lower():
        return f"Сметана - {ceil(int(num) * 0.13 / 2.2)} кг.\n"+ f"Вода - {int(int(num) * 0.13 / 2.88)} кг.\n" + f"Мука - {round(int(num) * 0.13 / 10)} кг.\n" + f"Масло - {format(int(num) * 0.13 / 33, '.1f')} кг.\n" + f"Соль - {format(int(num) * 0.13 / 100, '.1f')} кг.\n" + f"Чёрный перец - {format(int(num) * 0.13 / 500, '.3f')} кг.\n" + f"Красный перец - {format(int(num) * 0.13 / 769, '.3f')} кг.\n" +\
f"Сорбат - {format(int(num) * 0.13 / 1000, '.3f')} кг.\n"+ f"Аджика - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Хм-ли - {format(int(num) * 0.13 / 1250, '.3f')} кг.\n" + f"Укроп - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Паприка - {format(int(num) * 0.13 / 909, '.3f')} кг.\n" + f"Томат - {ceil(int(num) * 0.13 / 10)} банок."
    else:
        return "Я не знаю такой вид!!!"
