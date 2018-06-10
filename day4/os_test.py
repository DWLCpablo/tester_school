import os
from datetime import datetime

if __name__ == '__main__':
    print(os.name)
    print(os.uname())
    print(os.listdir('.')) # tak jak ls linuxowy, podajesz ścieżkę
    print(os.stat('data.json'))  # zwraca info nt pliku/katalogu, interesuje nas parametr 'size' (bajty). i st_time (kilka na końcu)
    stat = os.stat('data.json')
    print('Rozmiar: ', stat.st_size)
    atime = datetime.fromtimestamp(stat.st_atime)
    print('Ostatni dostęp: ', atime


def info(dir):
    info = []
    target = os.listdir(dir)
    stat = os.stat(dir)
    for i in target:
        info.append(i)
    for i in stat:
        info.append(i[-4])
    return info

print(info('/home'))