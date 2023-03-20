import collections

pets = {}
ask = ()


def command():
    print("""                  Добро пожаловать !!!
    - для создания новой записи о питомце введите команду - start - !
    - для поиска питомца по ID в базе данных введите команду - basa - ! 
    - выйти из программы команда - stop - !""")
    global com
    com = input('     ввод: ')
    id = 0

    def create():
        global col, vid, a, voz, w, name
        global w, q, voz
        w = []
        print()
        a = input('введите кличку нового питомца ')
        col = input('введите цвет питомца ')
        vid = input('введите вид или пароду питомца ')
        name = input('имя владельцa ')
        try:
            voz = int(input('возраст питомца '))
        except ValueError:
            def get_numb():
                while True:
                    try:
                        voz = int(input('введите положительное число '))
                    except ValueError:
                        print(' требуется чиcло ')
                    else:
                        break

            get_numb()
        if voz == 1:
            w = 'год.'
        elif 2 <= voz < 5:
            w = 'года.'
        elif 5 <= voz < 20:
            w = 'лет.'
        elif voz % 10 == 1:
            w = 'год.'
        elif 1 < voz % 10 < 5:
            w = 'года.'
        else:
            w = 'лет.'
        s = [['цвет ', col], ['вид питомца ', vid], ['по кличке', '"' + str(a) + '"'],
             ['возраст питомца ', str(voz) + ' ' + str(w)], ['Имя владельца ', name]]
        q = {}
        q[a] = dict(s)
        global pets
        pets[id] = dict(q)
        last = collections.deque(pets, maxlen=1)[0]
        pets[last] = dict(q)

    if com == 'start':
        while True:
            id += 1
            create()
            global col, vid, a, voz, w, name
            print(f"""  - !!! создана новая азапись о питомце ID {id} имя {a}:
 это {col} {vid} по кличке "{a}". Возраст {voz}{w} Имя владельца: {name}.""")

            print("""- желаете добавить следующую запись о питомце нажмите любую клавишу !!!- 
- что бы перейти в базу дааных,  введите basa !!!  """)
            com = input()
            if com == 'basa':
                break

    def read():
        ask = ()
        global pets
        try:
            ask = int(input('!введите ID питоца: '))
        except ValueError:
            def get_numb1():
                while True:
                    global ask
                    try:
                        ask = int(input('введите число соответствующее ID: '))
                    except ValueError:
                        print('принимается только целое число')
                    else:
                        break

            get_numb1()

        def rez():
            y = {}
            y.update(pets[ask])
            v = {}
            h = []
            for i in y.values():
                v.update(i)
                for f in v.values():
                    h.append(f)
                    # for d in gi.values():
                    # h.append(d)
            print(f'      - Это {h[0]} {h[1]} по кличке {h[2]} Возраст {h[3]} Влaделец {h[4]}. -')
            print()

        if ask in pets.keys():
            global k
            k = ask
            rez()
        return None if ask in pets.keys() else print('    - Нет такого ID в базе -')

    if com == 'basa':
        while com != 'stop':
            c = input(""" !для поиска по ID питомца нажмите любую клавишу!                                        
 !для для просмотра всего списка базы команда - list - ! 
 !!! для воврата в начало программы команда - back - !!!""")
            if c == 'list':
                global pets
                for i in pets:
                    for j in pets[i]:
                        print(pets[i])
            if c == 'back':
                command()
            read()
            print(""" !!! продолжить поиск в базе нажмите любую клавишу !!! 
 !!! для редактирования найденой записи команда - update - !!!
 !!! для воврата в начало программы команда - back - !!!""")
            c = input()
            if c == 'back':
                command()
            elif c == 'update':

                def update():
                    global k
                    global pets
                    while True:
                        y = {}
                        y.update(pets[k])
                        v = {}
                        h = []
                        for i in y.values():
                            v.update(i)
                            for f in v.values():
                                h.append(f)
                        print(f'- Это {h[0]} {h[1]} по кличке {h[2]} Возраст {h[3]} Влaделец {h[4]}. -')
                        print(f'Удалить запись {k}? yes мли no?')
                        del_te = input('введите yes или no : ')
                        if del_te == 'yes':
                                # pets.pop(k)
                            print(f' Запись {k} {h[0]} удалена из базы данных!')
                            pets.pop(k)
                            return
                        else:
                            command()

                update()
            else:
                read()
    if com != 'stop':
        command()


command()
