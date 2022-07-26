class Kalkulator:
  
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __del__(self):
        del self.a
        del self.b

    def dodawanie(self):
        return self.a + self.b

    def odejmowanie(self):
        return self.a - self.b
    
    def mnozenie(self):
        return self.a * self.b
    
    def dzielenie(self):
        if self.b != 0:
            return self.a / self.b 
        else: 
            print('Nie wolno dzielic przez zero!')
            return 0
 
    def wyswietlWynik(self, wynik):
        print (wynik)

a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))
kalkulator = Kalkulator(a,b)
      
wybor = input('Wybierz rodzaj dzialania: \n1 - + \n2 - - \n3 - * \n4 - /\n -> :')

if wybor == '1':
    wynik = kalkulator.dodawanie()
    kalkulator.wyswietlWynik(wynik)
elif wybor == '2':
    wynik = kalkulator.odejmowanie()
    kalkulator.wyswietlWynik(wynik)
elif wybor == '3':
    wynik = kalkulator.mnozenie()
    kalkulator.wyswietlWynik(wynik)
elif wybor == '4':
    wynik = kalkulator.dzielenie()
    kalkulator.wyswietlWynik(wynik)
else:
    print ('Nie ma takiej opcji')

del kalkulator #metoda __del__ zapobiega wyciekom pamieci, tzw. memory leaks - usuwa ona z pamieci operacyjnej obiekt kalkulator i pola a i b - WYCIEKI PAMIECI SA GROZNE, SZCZEGOLNIE GDY DANE TE SA DANYMI WRAZLIWYMI - moga one stac sie przedmiotem ataku hackerow
