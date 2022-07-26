lista1 = ["abc", "def" , "ghi" , "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ['xyz' , 1, '2']

print (lista1)
print (lista2)
print (lista3)

print (lista1[0])
print (lista1[3])

lista2[1] = lista3[1]

print(lista2[1])

lista3[2] = input("Wpisz jakas litere: ")
print(lista3)

lista1.append('slowo')
print (lista1)

del lista1[0]
print (lista1)

print(len(lista1))

lista1.extend(lista3)
print(lista1)

# list - lista, jeden ze sposobow na grupowanie zmiennych 
# dostepne sa tez krotki i slowniki 
# 'lista1' to lista o elementach wyrazonych w '[ ]' nawiasie kwadratowym
# te elementy moga byc dowolnego rodzaju
# aby wskazac cala liste, nalezy wpisac jej nazwe - print(lista1)
# aby wskazac ktorys z elementow listy wskazujemy jej nazwe oraz numer elementu (liczymy chyba od 0) - print(lista1[0]) - tak, pierwszy element jest oznaczony liczba 0
#NUMEROWANIE W INFORMATYCE ZACZYNAMY OD ZERA [0], 0 - JEST PIERWSZYM INDEKSEM...
# linia 12 - podmiana elementu lista2[1] = lista3[1] drugiego z listy2 na drugi z listy3
# aby powiekszac listy nalezy uzyc metody append, zob. <19> lista1.append('slowo') - dodaje element do istniejacej juz listy
# metoda extend() 'lista1.extend(lista3)' dodaje liste do drugiej listy - czyli tutaj chyba do listy1 dodaje liste3

# wazna informacja: programowanie obiektowe == metoda, uzywamy jej tak element.metoda()

# natomiast drugi rodzaj programowania ale nie jedyny programowanie strukturalne uzywa FUNKCJI
# funckcje zapisujemy tak funkcja(element)

# w obu przypadkach funkcja i metoda wywolywane sa dla elementu o nazwie element 



#----------------- pseudo-code /sudo code - kod zrozumialy dla wszystkich programistow -------------------#   

# FUNKCJE DO OPEROWANIA NA LISTACH:

# len(lista) - podaje dlugosc listy, len to funkcja (lista) to element 

# cmp(element1, element2) - porownuje dwa elementy listy compare - skrotowo cmp, to tez jest funkcja cmp()

# METODY DO OPEROWANIA NA LISTACH:

# lista.count(element) - sprawdza ile razy dany element wystepuje w liscie - to metoda, zaczyna sie od elementu 'lista', pozniej jest zadanie dzialania na tym obiekcie 'count' i nastepnie co jest przedmiotem dzialania (element) 

# lista.insert(index, element) - wstawia do listy element pod numerem index (indeksowanie zaczyna sie w od 0, zero jest pierszym indeksem) - tutaj na obiekcie 'lista' zostanie przeprowadzona operacja insert - wstaw, nastepnie w nawiasie okreslamy pod ktorym indeksem zostanie wstawiony element

# lista.remove(element) - usuwa element z listy (zamiast 'remove' mozna uzyc slowa 'del')