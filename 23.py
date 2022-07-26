import sys

print ('witaj w prostym kalkulatorze')
a = int(input ('podaj pierwsza liczbe: '))
b = int(input ('podaj druga liczbe: '))
if (b == 0):
    print ("nie wolno dzielic przez 0!"), exit ()


wynik = a / b 
c = input ('jesli chcesz otrzymac tylko liczby calkowite, wybierz 1, przeciwnie wybierz 2: ')

if (c == "1"):
    print (int(wynik))

elif (c == "2"):
    print (float(wynik))
