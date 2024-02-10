from customtkinter import *

class Calculadora(CTk):
    def __init__(self):
        super().__init__()
        self.title = ("Calculadora Python")
        self.geometry = ("500x600")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
    