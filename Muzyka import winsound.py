import winsound

tytul = input('podaj nazwe pliku do odtworzenia: ')

winsound.PlaySound (tytul, winsound.SND_FILENAME)