plik1 = open ('plik1', 'wb')

plik1.close()


plik1 = open ('plik1', 'ab')

x = (input('wpisz liczbe:'))
plik1.write(x)
plik1.close()

plik1 = open ('plik1', 'rb')

print(plik1)
#zjebalem