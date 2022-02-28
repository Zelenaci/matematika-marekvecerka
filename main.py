from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import (Label, Button, Scale, HORIZONTAL, Canvas, Frame, Entry, LEFT, RIGHT, N, S, E ,W, StringVar, IntVar)

class Application(tk.Tk):
    #name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"

   
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.varEntry = tk.StringVar()
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0,padx = 10, pady = 10)

        self.lbl1 = tk.Label(self.frame, text="A")
        self.lbl1.grid(row=0, column=0, ipadx = 5, ipady = 5)
        self.lbl1.config(font=(20))
        
        self.lbl3 = tk.Label(self.frame, text="+", width=10)
        self.lbl3.config(font=(20))
        self.lbl3.grid(row=0, column=1, ipadx = 5, ipady = 5)

        self.lbl2 = tk.Label(self.frame, text="B")
        self.lbl2.grid(row=0, column=2, ipadx = 5, ipady = 5)
        self.lbl2.config(font=(20))

        self.entry = tk.Entry(self.frame, textvariable = self.varEntry)
        self.entry.grid(row=0, column=3, padx = 5, pady = 5)

        self.btnOvěřit = tk.Button(self.frame, text="Ověřit", command=self.overeni)
        self.btnOvěřit.grid(row=0, column=4, padx = 5, pady = 5)

        self.btn1 = tk.Button(self.frame, text="Konec", command=self.konec)
        self.btn1.grid(row=0, column=5, padx = 5, pady = 5)

        self.priklad()

    def priklad(self):
        vysledek = random.choice([self.plus, self.minus, self.krat, self.deleno])
        return vysledek()
    

    def overeni(self, event = None):
        try:
            zadanyvysledek = int(self.varEntry.get())
        except:
            zadanyvysledek = ""
        if self.vysledek == zadanyvysledek:
            self.config(background="#00ff00")
            print("Správně")
        else:
            self.config(background="#ff0000")
            print("Špatně")
        self.priklad()

    def plus(self):
        self.cisloA = random.randint(1,49)
        self.cisloB = random.randint(1,49) 
        self.vysledek = self.cisloA + self.cisloB
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text = self.cisloB)
        self.lbl3.config(text = "+")
        return self.vysledek

    def minus(self):
        self.cisloA = random.randint(1,100)
        self.cisloB = random.randint(1,self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text = self.cisloB)
        self.lbl3.config(text = "-")
        return self.vysledek

    def krat(self):
        self.cisloA = random.randint(1,9)
        self.cisloB = random.randint(1,9)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text = self.cisloB)
        self.lbl3.config(text = "*")
        return self.vysledek

    def deleno(self):
        self.vysledek = random.randint(1,9)
        self.cisloB = random.randint(1,9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text = self.cisloB)
        self.lbl3.config(text = "/")
        return self.vysledek 
    
    def generuj(self):
        funkce =random.choice([self.plus, self.minus, self.krat, self.deleno])
        funkce()

    def konec(self, event=None):
        super().quit()


app = Application()
app.mainloop()