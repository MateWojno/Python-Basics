import sys
print ('To prosty program do dzielenia liczb dodatnich.')

a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))

if (a != 0 and a > 0) and (b != 0 and b> 0):
    wynik = a / b 
    print ('wynik tego dzialania to: ', wynik), sys.exit ()
    