from serializacja import *

print ('Witaj w programie do obslugi gosci hotelowych')

wybor = -1

while (wybor != 0):
    wybor = int(input("\nWybierz opcje:\n1 - dodaj nowego goscia\n2 - usun goscia\n3 - znajdz goscia\n0 - zakoncz dzialanie programu\n -> :"))

    if (wybor == 1):
        dodajGoscia()
    elif (wybor == 2):
        nazwisko = input('\nPodaj naziwks')