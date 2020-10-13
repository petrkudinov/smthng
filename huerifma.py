huedict = {
    'а': 'я',
    'ы': 'и',
    'о': 'ё',
    'у': 'ю',
    'э': 'е',
    'я': 'я',
    'и': 'и',
    'ё': 'ё',
    'ю': 'ю',
    'е': 'е',
}
            
a = ''
while True:
    a = str(input().lower())
    cnt = 1
    for i in a:        
        if i in 'аыоуэяиёюе':
            verb = ('ху' + huedict.get(i) + a[cnt:])
            print(verb)
            break
        else:
            cnt += 1
