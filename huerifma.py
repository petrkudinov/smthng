cnt = 0
a = ''
while a != 'хуй':
    a = str(input())
    if a == 'хуй':
        print('лучшая рифма к слову "хуй" - "хуй"')
        cnt += 1
    elif a[0] == 'а':
        print('ху', end='')
        print('я', end='')
        print(a[1:])
        cnt += 1
    elif a[0] == 'ы':
        print('ху', end='')
        print('и', end='')
        print(a[1:])
        cnt += 1
    elif a[0] == 'о':
        print('ху', end='')
        print('ё', end='')
        print(a[1:])
        cnt += 1
    elif a[0] == 'у':
        print('ху', end='')
        print('ю', end='')
        print(a[1:])
        cnt += 1
    elif a[0] == 'э':
        print('ху', end='')
        print('е', end='')
        print(a[1:])
        cnt += 1        
    elif a[0] == 'я':
        print('ху', end='')
        print(a[0:])
        cnt += 1
    elif a[0] == 'ё':
        print('ху', end='')
        print(a[0:])
        cnt += 1
    elif a[0] == 'ю':
        print('ху', end='')
        print(a[0:])
        cnt += 1
    elif a[0] == 'е':
        print('ху', end='')
        print(a[0:])
        cnt += 1        
    elif a[1] == 'а':
        print('ху', end='')
        print('я', end='')
        print(a[2:])
        cnt += 1
    elif a[1] == 'ы':
        print('ху', end='')
        print('и', end='')
        print(a[2:])
        cnt += 1
    elif a[1] == 'о':
        print('ху', end='')
        print('ё', end='')
        print(a[2:])
        cnt += 1
    elif a[1] == 'у':
        print('ху', end='')
        print('ю', end='')
        print(a[2:])
        cnt += 1
    elif a[1] == 'э':
        print('ху', end='')
        print('е', end='')
        print(a[2:])
        cnt += 1
    else:
        print('ху', end='')
        print(a[1:])
        cnt += 1
