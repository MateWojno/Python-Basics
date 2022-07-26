import winsound
print (' Zagrajmy w gre, rozwiaz ponizszy warunek logiczny, znajac wartosci a=0, b=1, c=1, d=1. Jezeli ( a < 0 lub b > 0) i (c rozne od 0 albo d) to zdanie jest w zupelnosci prawdziwe czy falszywe??')
e = input("wpisz odpowiedz: falsz, prawda: ")
if e == "falsz":
    print ('Prawie dobrze hehe') 
elif e == "prawda":
  print ('Wygrales talon...')
  # zagramy cos hehe #
   # winsound.PlaySound(tytul, winsound.SND_FILENAME)
winsound.PlaySound('falsz', winsound.SND_FILENAME) 