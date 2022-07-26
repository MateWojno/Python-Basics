print ('To prosty program do obliczania kwoty obnizonej o nalezny podatek dochodowy')
podatekA = 10/100
podatekB = 20/100
podatekC = 30/100

def obliczPodatek(zarobki):
    if (zarobki < 2000):
        podatek = podatekA
    elif (zarobki >= 2000 and zarobki < 5000):
        podatek = podatekB
    else:
        podatek = podatekC
    return podatek * zarobki

zarobki = int(input('Podaj wysokosc swojego dochodu: '))
wysokoscPodatku = obliczPodatek(zarobki)
print ("Wysokosc twojego podatku to: ", wysokoscPodatku)