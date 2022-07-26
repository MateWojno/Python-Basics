class Dane:

    __pesel = '123456789'
    __nip = '777-777-77-77'

    def __init__(self):
        print ('Obiekt utworzony')
    def __del__(self):
        del Dane.__pesel
        del Dane.__nip
        print('Obiekt usuniety')
    
    def wyswietlDane(self):
        self.__wyswietl()
    
    def __wyswietl(self): #ukryta metoda! - przydatna rzecz, odpalana za pomoca metody posredniej - wyswietlDane()
        print (self.__pesel)
        print(self.__nip)
    
dane = Dane()

dane.wyswietlDane()

del dane 
        