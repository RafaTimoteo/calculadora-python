from customtkinter import *

class Calculadora(CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Python")
        self.geometry("400x500")
        self.create_widgets()
    
    def create_widgets(self):
        #Campo de caracteres
        self.entry = CTkEntry(self, font=('Helvetica', 40), justify=RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 4, padx=3, pady=3, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Lista de botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        #Criação dos botões
        for (texto, linha, coluna) in botoes:
            butao = CTkButton(self, font=('Helvitica', 30), text=texto, command = lambda t=texto: self.click(t))
            butao.grid(row=linha, column=coluna, padx=2, pady=2, sticky='nsew')
            self.grid_rowconfigure(linha, weight=1)
            self.grid_columnconfigure(coluna, weight=1)

    def click(self, value):
            valor_entry = self.entry.get()

            if value == '=':
                 try:
                    resultado = eval(valor_entry)
                    self.entry.delete(0, END)
                    self.entry.insert(END, str(resultado))
                 except:
                      self.entry.delete(0, END)
                      self.entry.insert(END, "Erro")
            else:
                 self.entry.insert(END, value)


        
if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
