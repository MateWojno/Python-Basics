krotka1 = ("abc", "def", "ghi", "jkl")

print (krotka1)
print (krotka1[1]) # 'drukuje' drugi element krotki 1 (index 1, indeksowanie zaczynamy od 0)
print (krotka1[1:2]) # elementy z indeksami od 1 - 2, czyli element drugi i trzeci krotki

krotka2 = ('xyz',) # ten przecinek jest niezbedny
krotka3 = krotka1 + krotka2

print (krotka3)

lista = list(krotka3) #konwersja krotki na liste
lista.append("slowo") #dodajemy nowy element do listy

print(lista) #listy i krotki to struktury sekwencyjne, każda z nich posiada kolejnosc i przypisany index - sa uporzadkowane, natomiast nieuporzadkowany "worek, do którego wrzucilismy dane to slownik 


# w jezyku python oprocz list dostepne sa krotki, roznia sie one od list tym, ze nie mozna ich edytowac!
# mozna zamienic krotke w liste za pomoca funckji list(krotka)
# a w druga strone mozna zamienic liste w krotke przy uzyciu funkcji 'tuple(lista)'
# Krotka (ang. tuple) – struktura danych będąca odzwierciedleniem matematycznej n-ki, tj. uporządkowanego ciągu wartości. Krotki przechowują stałe wartości o różnych typach danych – nie można zmodyfikować żadnego elementu, odczyt natomiast wymaga podania indeksu liczbowego żądanego elementu.  