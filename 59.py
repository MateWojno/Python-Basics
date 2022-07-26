import tkinter

okno = tkinter.Tk()
etykietaWitaj = tkinter.Label(okno, text='Witaj')
przyciskZamknij = tkinter.Button(okno, text='Zamknij', command=okno.destroy)
etykietaWitaj.pack()
przyciskZamknij.pack()
okno.mainloop()