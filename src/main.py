from classes import Converter
import customtkinter
import os





customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("550x450")
janela.title("App Converter")


icon_path = os.path.abspath("../src/assets/moeda.ico")
janela.iconbitmap(icon_path)







#funções




def converta():
   valor = str(caixa_texto.get())
   valor = valor.replace(',','.')
   valor = float(valor)
   conversor = Converter(valor)
   conversor.utilizando_cotacao()
   exibir(conversor)


def exibir(conversor):
   resultado = "US$ " + str(conversor.valor_convertido)
   texto.configure(text= resultado, )


 
#Criando a caixa de input
caixa_texto = customtkinter.CTkEntry(janela, placeholder_text="R$ 0,00")
caixa_texto.pack(padx=10, pady=10, )

#altera a posição do objeto
caixa_texto.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

#Criando o texto onde vai constar o valor convertido
texto = customtkinter.CTkLabel(janela, text="US$ 0.00")
texto.pack(padx = 10, pady = 10)
texto.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

#botao

button_us = customtkinter.CTkButton(janela, text="US$", command=converta)
button_us.pack(padx = 10, pady= 10)
button_us.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

janela.mainloop()
