a = "nazwa programu: 27-S"
print (a)
b = int(input ('wybór dzialania: 1 - dodaj, 2 - odejmij, 3 - dziel, 4 - mnoz: '))
c = int (input('wpisz piersza liczbe: '))
d = int (input('wpisz druga liczbe: '))
if (b == 1):
    wynik = c + d 
elif (b == 2):
    wynik = c - d 
elif (b == 3):
    wynik = c / d 
elif (b == 4):
    wynik = c * d  
else:
    print ('Error 404'), exit ()
print ('wynik dzialania to: ', wynik )