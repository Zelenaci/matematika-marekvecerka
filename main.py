#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def generuj(self):
        self.funkce = random.choice([self.plus, self.minus, self.krat, self.delete])
        self.funkce()
        if self.funkce == self.minus:
            print("Jo")
        else:
            print("Ne")



    def plus():
            # vygeruje příklad na scčítání
            self.cisloA = random.randint(1,99)
            self.cisloB = random.randint(1,99)
            self.vysledek = self.cisloA + self.cisloB
    def close(self):
        self.destroy()
    
    def krat(self):
        self.lbl.config(text="*")

    def deleno():
        #Vygeneruje příklad na celočíselné dělen

            self.cisloB = random.randint(1,9)
            self.vysledek = random.randint(1,9)
            self.cisloA = self.cisloB  - self.vysledek
            self.lbl.config(text='/')


    def close(self):
        self.plus()
    

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()

    def about(self):
     oainloop()
