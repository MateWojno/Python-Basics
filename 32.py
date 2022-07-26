from pkgutil import ImpImporter


def wyswietl (imie, nazwisko):
    print ("Twoje imie i nazwisko to:", imie, nazwisko)
    return

imie = input('Wpisz imie: ')
nazwisko = input('Wpisz nazwisko: ')

wyswietl(imie, nazwisko)