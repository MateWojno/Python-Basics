class KlasaGlowna:
    
    imie = "Mateusz"
    nazwisko = "Wojno"

    def __init__(self):
        print ('Obiekt klasy glownej utworzony')
    def __del__ (self):
        del KlasaGlowna.imie
        del KlasaGlowna.nazwisko
        print ('Obiekt klasy glownej usuniety')
    def wyswietlDane(self):
        print (imie + "" + nazwisko)

class klasaDziedziczaca (KlasaGlowna):

        pesel = "123456789"
        nip = "777-777-77-77"

        def __init__(self):
            print ('Obiekt klasy dziedziczacej utworzony')
        def __del__(self):
            del klasaDziedziczaca.pesel 
            del klasaDziedziczaca.nip
            print ('Obiekt klasy dziedziczacej usuniety')
obiekt1 = KlasaGlowna()
obiekt2 = klasaDziedziczaca()

print("imie =", obiekt1.imie)
print('nazwisko =', obiekt1.nazwisko)

print('imie =', obiekt2.imie)
print('nazwisko =', obiekt2.nazwisko)
print('pesel =', obiekt2.pesel)
print('nip', obiekt2.nip)

del obiekt1
del obiekt2

    