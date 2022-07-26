import string

def sprawdz (liczba):
    poziom = 0
    if liczba.isdigit() == False:
        if liczba.isupper() == True:
            raise Exception(-1)
            poziom = -1
        elif liczba.islower() == True:
            raise Exception(-2)
            poziom = -2
        else: 
            raise Exception(-3)
            poziom = -3

    return poziom

try:
    liczba = input('Podaj liczbe:')
    sprawdz(liczba)
    print('OK. Uzytkowanik podal liczbe.')
except Exception as e:
    print ('Blad = ', e.args[0])