 dane = input('podaj dane do zapisu:')

 try:
    plik = open ('X:\plik.txt', 'w')
    plik.write(dane)
except Exception:
    print ('Nie udalo sie zapisac danych.')
else:
    plik.close()
#nie dziala!