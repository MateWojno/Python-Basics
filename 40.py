#petla while 
print ('Ten program dodaje 10 kolejno podanych przez Ciebie liczb, zacznij teraz.')
wynik = 0 
x = 1 
while x <= 10:
    liczba = int(input("Podaj kolejna liczbe: "))
    wynik  += liczba 
    x += 1
print ('Wynik dodawania to: ', wynik)
# 'wynik' to zmienna która przechowuje sumę kolejnych liczb
# zmienna 'x' odpowiada za to ile razy nasza petla ma sie wykonac 
# petla while w linii 5 oraz warunek jak dlugo ma sie wykonywac 
# warunek - wykonuj petle dopóki liczba x jest mniejsza równa  10
# x += 1 to zwiekszanie 'x' o 1 za kazdym razem, gdy petla sie wykona 
# w pythonie jest jeszcze inna petla 'for'