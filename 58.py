from kalkulator import *  #oznacza to z modulu o nazwie kalkulator zaimportuj wszystko '*' oznacza 'wszystko', jezeli modul/lib znajdowalby sie w innym katalogu, nalezaloby podac sciezke do niego
a = int(input('Podaj pierwsza liczbe:'))
b = int(input('Podaj druga liczbe: '))

wyborDzialania = int(input('Podaj rodzial dzialania:\n 1 - dodawanie\n 2 - odejmowanie \n 3 - mnozenie \n 4 - dzielenie\n -> :'))

if (wyborDzialania == 1):
    print(dodaj(a,b))
elif (wyborDzialania == 2):
    print(odejmij(a,b))
elif (wyborDzialania == 3):
    print(pomnoz(a,b))
elif (wyborDzialania == 4):
    print (podziel(a,b))
else:
    print('Nie ma takiej opcji!')