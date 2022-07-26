print ('witaj w prostym kalkulatorze')
a = int(input('podaj pierwsza liczbe: '))
b = int(input('podaj druga liczbe: '))
c = (input('wybierz rodzaj dzialania: +  dodawanie, -  odejmowanie, *  mnozenie, /  dzielenie: '))
if (c == "+"):
    wynik = a + b
elif (c == '-'):
    wynik = a - b
elif (c == '*'):
    wynik = a * b
elif (c == '/'):
    wynik = a / b 
else: print ('Dokonales zlego wyboru...'), exit()

print ('Wynik dzialania to:', wynik)
