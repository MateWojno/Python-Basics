print ('Program dodajacy tylko liczby podzielne przez 3.')
wynik = 0 
while wynik < 100:
    liczba = int(input('Podaj kolejna liczbe dodatnia: '))
    if (liczba < 0):
        print ("liczba musi byc dodatnia!")
        break
    if (liczba % 3 == 0):
        wynik += liczba 
    else:
        continue
print ('Wynik to: ', wynik)

# 'x += y' powieksza o zmienna x o wartosc y  