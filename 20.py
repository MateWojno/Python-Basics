from time import clock_settime


c1 = input ('wpisz dwie pierwsze cyfry aktualnego roku: ')
c2 = input ('wpisz dwie ostatnie cyfry aktualnego roku: ')
wiek = int(input ('wpisz swoj wiek: '))

print (c1 + c2)
c3 = int(c1+c2)
print (c3-wiek)
