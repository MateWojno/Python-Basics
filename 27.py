from logging import root


print ('Witaj w prostym programie porownujacym liczby, a nastepnie wykonujacym dzielenie wiekszej przez mniejsza')
a = int(input('podaj pierwsza liczbe: '))
b = int(input('podaj druga liczbe: '))

if (a == 0) or (b == 0):
    wynik = "error"    
elif (a > b): 
    wynik = a / b
elif (b > a):
    wynik = b / a 
else:
   print ('Wynik dzialania to : 1'),   exit ()
print ('wynik dzialania to: ', wynik)
