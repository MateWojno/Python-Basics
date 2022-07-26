import string

def sprawdz (liczba):
    poziom = 0
    if liczba.isdigit() == False:
        raise Exception(-1)
        poziom = -1
    return poziom

try:
    liczba = input('Podaj liczbe:')
    sprawdz(liczba)
    print('OK. Uzytkowanik podal liczbe.')
except Exception as e:
    print ('Blad = ', e.args[0])