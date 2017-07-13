names = ['mark', 'lala', 'nana', 'katarina', 'jessica']


for name in names:
    if(name == 'nana'):
        print(f'skip {name}')
        continue

    if(name == 'katarina'):
        print(f'found {name}')
        break
    print(f'looking at {name}')