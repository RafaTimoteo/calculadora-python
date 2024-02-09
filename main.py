from customtkinter import *


app = CTk()

#Estrutura da Janela
app.title('Calculadora Python')
app.geometry('500x470+500+100')
app.resizable(width=False, height=False)

#Campo dos numeros
camp_num = CTkEntry(app, width = 300)
camp_num.place(x = 100, y = 25)



app.mainloop()