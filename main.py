import os
from datetime import datetime

if not os.path.exists('result'):
    os.mkdir('result')

def sorter(path, domain):
    try:
        f = open(path, 'r', encoding='utf-8')
        s = len(f.readlines())
        print(f'{s} lines')
        f.close()
        time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        os.mkdir(f'result/{time}')
        c = open(f'result/{time}/{domain}.txt', 'w', encoding='utf-8')
        ehem = 0
        with open(path, 'r', encoding='utf-8') as f:
            for x in range(s):
                ae = f.readline()
                a = ae.split(':')[0].split('@')[-1]
                if a == f'{domain}':
                    c.write(f'{ae}')
                    ehem = ehem + 1
        return (ehem)
    except:
        print('Error.Probably wrong encoding or file too big')

def mainmenu():
    path = input('Main Menu\n\n\ndrop the file here\n').strip('"')
    os.system('cls')
    domain = input('Main Menu\n\n\ndomain\n')
    os.system('cls')
    print(f'{domain} : {sorter(path, domain)}')

mainmenu()
ar = input()
