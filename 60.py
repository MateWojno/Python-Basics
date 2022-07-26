from tkinter import *

def dodaj():
    print(int(poleA.get()) + int(poleB.get()))
    poleA.delete(0,END)
    poleB.delete(0,END)

okno = Tk()
Label (okno, text='Liczba nr 1: ').grid(row=0)
Label (okno, text='Liczba nr 2: ').grid(row=1)

poleA = Entry(okno)
poleB = Entry(okno)

poleA.grid(row=0, column=1)
poleB.grid(row=1, column=1)

przyciskDodaj = Button(okno, text='Dodaj', command=dodaj)
przyciskDodaj.grid(row=3, column=0, sticky= W, pady= 4)
przyciskWyjdz = Button(okno, text="Wyjdz", command=okno.destroy)
przyciskWyjdz.grid(row=3, column=1, sticky=W, pady=4)

mainloop()