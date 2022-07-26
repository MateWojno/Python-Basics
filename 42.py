szukanaLiczba = int(input('Podaj liczbe, ktora ma znalezc uzytkownik: '))
strzal = 0
while strzal != szukanaLiczba:
    strzal = int(input("Odgadnij szukana liczbe: "))
    if (strzal < szukanaLiczba):
        print ("Za malo!")
        continue
    elif (strzal > szukanaLiczba):
        print ("Za duzo!")
        continue
    print ('Ostatnie wykonanie petli')
print ("Brawo, wygrales!") 
# Jak zabezpieczyc int przed wpisaniem liter??
# slowo continue - zastosowane wewnatrz petli powoduje ponowne wykonanie petli 