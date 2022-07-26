class PoleFigury:

    def __init__(self):
        print ('Obiekt klasy PoleFigury utworzony')
    def __del__(self):
        print('Obiekt klasy PoleFigury usuniety')
    
    def obliczPole(self):
        print ()

class PoleTrojkata(PoleFigury):

    def __init__(self):
        print('Obiekt klasy PoleTrojkata utworzony')
    def __del__(self):
        del self.a
        del self.h
        print ('Obiekt klasy PoleTrojkata usuniety')
    def obliczPole(self):
        self.a = int(input('Podaj a:'))
        self.h = int(input('Podaj h:'))
        print('Pole trojkata=', 0.5 * self.a * self.h)
    
class PoleProstokata(PoleFigury):

    def __init__(self):
        print('Obiekt klasy PoleProstokata utworzony')
    def __del__(self):
        del self.a
        del self.b
        print('Obiekt klasy PoleProstokata usuniety')
    
    def obliczPole(self):
        self.a = int(input('Podaj a:'))
        self.b = int(input('Podaj b:'))
        print ('pole prostokata =', self.a * self.b)
    

wybor = int(input('Oblicz pole: 1 - trojkata, 2 - prostokata: '))

if wybor == 1:
        trojkat = PoleTrojkata()
        trojkat.obliczPole()
        del trojkat
elif wybor == 2:
        prostokat = PoleProstokata()
        prostokat.obliczPole()
        del prostokat
else:
        print('Nie ma takiej figury!')