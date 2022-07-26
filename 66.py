class Dane:
    pesel = "123456789"
    __nip = "777-777-777" # do tej zmiennej nie ma dostepu na zewnatrz klasy, poprzez uzycie "__", w ten sposob dostep do danych __nip jest mozliwy jedynie przez uzycie metody wyswietlNip(self)

    def __init__(self):
        print ('Obiekt utworzony')
    def __del__(self):
        print ('Obiekt usuniety')

    def wyswietlNip(self):
        print(self.__nip)

dane = Dane()

print(dane.pesel)
dane.wyswietlNip()

del dane