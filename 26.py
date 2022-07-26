print ('Witaj w prostym kalkulatorze')
a = int(input('podaj pierwsza liczbe: '))
b = int(input('podaj druga liczbe: '))
c = int(input('wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 5 - potegowanie, 6 - pierwiastkowanie <jeszcze nie dziala>: '))

if (c == 1):
    wynik = a + b
elif (c == 2):
    wynik = a - b
elif (c == 3):
    wynik = a * b
elif (c == 5):
    wynik = a ** b 
elif ((b == 0), (c == 4)):
    wynik = "nic z tego"     
elif (c == 4):
    wynik = a / b
elif (c == 6):
    wynik = a // b
else:
    print ('zacznij jeszcze raz'), exit ()
print ('wynik dzialania to: ', wynik)
