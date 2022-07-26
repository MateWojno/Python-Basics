import sys

print ('witaj w prostym kalkulatorze')
a = int(input ('podaj pierwsza liczbe: '))
b = int(input ('podaj druga liczbe: '))
if (b == 0):
    print ("nie wolno dzielic przez 0!"), 
    sys.exit ()
c = int(input ('wpis kod dzialania : dzielenie - 1, potegowanie -2, pierwiastkowanie -3: '))
if (c == 1):
    wynik = a / b
elif (c == 2):
    wynik = a ** b
elif (c == 3):
    wynik = a // b 
else:
    print('prosze spierdalac') 

 
d = int(input ('jesli chcesz otrzymac tylko liczby calkowite, wybierz 1, przeciwnie wybierz 2: '))

if (d == "1"):
    print (int(wynik))

elif (d == "2"):
    print (float(wynik))
