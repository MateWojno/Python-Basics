class KlasaGlowna: #nazwa klasy zawsze z wielkiej litery

    imie = "Max"
    nazwisko = 'Wojno'

    def __init__(self):
        print ('Obiekt klasy glownej utworzony')
    def __del__ (self):
        del KlasaGlowna.imie
        del KlasaGlowna.nazwisko
        print('Obiekt klasy glownej usuniety')
    
    def wyswietlDane(self): 
