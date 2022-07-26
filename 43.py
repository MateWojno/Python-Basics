print ('Program dodajacy tylko liczby parzyste.')
wynik = 0 
while wynik < 100:
    liczba = int(input('Podaj kolejna liczbe dodatnia: '))
    if (liczba < 0):
        print ("liczba musi byc dodatnia!")
        break
    if (liczba % 2 == 0):
        wynik += liczba 
    else:
        continue
print ('Wynik to: ', wynik)
#  fajny program - warto dokladnie czytac instrukcje 
# '%' operator 'modulo' - jest to dzialanie, ktore dzieli pierwsza liczbe przez druga i jesli zostanie jakas reszta to ja zwraca a jesli nie zostanie to zwraca 0
# operator modulo jest uzywany tez w KW - skrypcie!
# poczytajmy o tym operatorze wiecej - czy tutaj liczba % 2 == 0 oznacza liczbe podzielna przez dwa bez reszty? 
# co w tym operatorze oznacza reszta??