plik = open("plik.txt", 'w+', 'a+')
plik.write('Pierwsze zdanie\n')
zawartosc = plik.read()
plik.close()

print(zawartosc)