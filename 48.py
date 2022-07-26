slownik = {"imie": "Michal", "nazwisko": "Wiszniewski", "wiek" :  31}
print (slownik["imie"])

slownik["imie"] = 'Mateusz' #slownik, zarowno jak liste mozna edytowac, slownik zbiera dane zbiorem par, nie jest zbiorem elementow a zbiorem par - czyli ELEMENTU oraz KLUCZA
slownik["zawod"] = 'programista'
print (slownik)

del slownik["nazwisko"]
print (slownik)

slownik["nazwisko2"] = 'Wojno'
print(slownik)
# NIEDOPUSZCZALNE JEST WSTAWIANIE ELEMENTOW O TAKICH SAMYCH KLUCZACH. Klucz musi byc niepowtarzalny, moze byc liczba, ciagiem znakow, a nawet krotka, ale musi byc unikatowy. - czy ten klucz to key, czy id - w pseudo code?