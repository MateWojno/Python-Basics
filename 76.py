import pickle

print('Witaj w programie zapisujacym dane gosci hotelowych')

daneGoscia = []
daneGosci = {}

daneGoscia.append(input("\nPodaj imie: "))
daneGoscia.append(input("\nPodaj nazwisko: "))
daneGoscia.append(input('\nPodaj adres: '))
daneGosci = {0 : daneGoscia}

print (daneGosci)

with open ('plik.binarny', "wb") as plik1:
    pickle.dump(daneGosci, plik1)

with open ('plik.binarny', "rb") as plik2:
    kopiaSlownika = pickle.load(plik2)

print (kopiaSlownika)

