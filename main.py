from customtkinter import *

class Calculadora(CTk):
    def __init__(self):
        super().__init__()
        self.title = ("Calculadora Python")
        self.geometry = ("500x600")
        self.create_widgets()
    
    def create_widgets(self):
        #Campo de caracteres
        self.entry = CTkEntry(self, font=('Helvetica', 20), justify=RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = NSEW)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
