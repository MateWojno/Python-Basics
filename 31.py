import sys

def dodawanie (a, b):
    return a + b
     

def odejmowanie (a, b):
    return a - b 
     

def mnozenie (a, b):
    return a * b
    

def dzielenie (a, b): 
    return a / b 
     

def zlyWybor():
    print ('Dokonales zlego wyboru!')
    sys.exit()

a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))
c = int(input('Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie: '))

if (c == 1):
    wynik = dodawanie(a, b)
elif (c == 2):
    wynik = odejmowanie (a, b)
elif (c == 3):
    wynik = mnozenie (a, b)
elif (c == 4):
    wynik = dzielenie (a, b)
else:
    zlyWybor()

print ('Wynik dzialania to: ', wynik)