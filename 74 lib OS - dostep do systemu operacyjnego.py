import os
from os.path import join

szukanyPlik = input('Podaj nazwe pliku, ktorego szukasz:')
sciezka = input('podaj sciezke, gdzie chcesz szukac pliku:')

for root, dirs, files in os.walk(sciezka):
    print('szukam: ', root)
    if szukanyPlik in files:
        print ('Plik znaleziony: %s' %join(root, szukanyPlik))
        break