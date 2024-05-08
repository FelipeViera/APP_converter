from classes import Converter
import customtkinter
import os
from PIL import Image




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("550x450")
janela.title("App Converter")


janela.resizable(width=False, height=False)

icon_path = os.path.abspath("../src/assets/moeda.ico")
janela.iconbitmap(icon_path)


simbolo = 'US$'




#funções

def usd():
   global simbolo
   simbolo = 'US$'
   converta('USD')

def eur():
   global simbolo
   simbolo = '€'
   converta('EUR')

def lib():
   global simbolo
   simbolo = '£'
   converta('GBP')

def converta(moeda):
   valor = str(caixa_texto.get())
   valor = valor.replace(',','.')
   valor = float(valor)
   conversor = Converter(valor)
   conversor.utilizando_cotacao(moeda)
   exibir(conversor)


def exibir(conversor):
   resultado = simbolo + " " + str(conversor.valor_convertido)
   texto.configure(text= resultado, )



#Imagem:
my_img = customtkinter.CTkImage(light_image=Image.open('../src/assets/capa.jpg'), size=(200, 200))
my_label = customtkinter.CTkLabel(janela, text="", image=my_img)
my_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
my_label.pack(padx=10, pady=15)


#Criando a caixa de input
caixa_texto = customtkinter.CTkEntry(janela, placeholder_text="R$ 0,00")
caixa_texto.pack(padx=10, pady=10, )


#altera a posição do objeto
caixa_texto.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

#Criando o texto onde vai constar o valor convertido
texto = customtkinter.CTkLabel(janela, text="US$ 0.00")
texto.pack(padx = 10, pady = 10)
texto.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)



#botao Dólar

button_us = customtkinter.CTkButton(janela, text="US$", command=usd, height=30, width=30, border_width=0 )
button_us.pack(padx = 10, pady= 10)
button_us.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

# Botão Euro

button_eur = customtkinter.CTkButton(janela, text="€", command=eur, height=30, width=30, border_width=0 )
button_eur.pack(padx = 10, pady= 10)
button_eur.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

# Botão Libra

button_eur = customtkinter.CTkButton(janela, text='£', command=lib, height=30, width=30, border_width=0 )
button_eur.pack(padx = 10, pady= 10)
button_eur.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)


janela.mainloop()
