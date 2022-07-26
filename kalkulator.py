#biblioteka w pythonie nazywana jest modułem#
#chuj, wole nazywac to library

def dodaj (a,b):
    return a + b

def odejmij (a,b):
    return a - b

def pomnoz (a,b):
    return a * b 

def podziel (a, b):
    if (b == 0):
        print ('Nie wolno dzielic przez 0')
        return 0
    return a / b