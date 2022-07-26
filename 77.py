import pickle

daneGoscia = []
daneGosci= {}

for i in range(5):
    daneGoscia.append(i)
    daneGoscia.append(input("\nPodaj imie: "))
    nazwisko = input("\nPodaj naziwsko: ")
    daneGoscia.append(input('\nPodaj adres: '))
    daneGosci.update({nazwisko : daneGoscia})
    daneGoscia = []

with open ("plik.binarny", "wb") as plik1:
    pickle.dump(daneGosci, plik1)

with open ("plik.binarny", "rb") as plik2:
    kopiaSlownika = pickle.load(plik2)

print (kopiaSlownika)