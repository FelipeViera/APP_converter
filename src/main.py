from classes import Converter
import customtkinter
import os
from PIL import Image




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("550x450")
janela.title("Real Converter")


janela.resizable(width=False, height=False)

icon_path = os.path.abspath("../src/assets/moeda.ico")
janela.iconbitmap(icon_path)


simbolo = 'US$'
entrada = ''


#funções
def brl():
   global simbolo
   global entrada
   if (entrada == ''):
      entrada = 'BRL'
      button_real.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)
      button_real.configure(height=20)


   elif (entrada == 'BRL'):
      entrada = ''
      button_real.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)
      button_real.configure(height=30)

   else:

      simbolo = 'R$'
      converta('BRL')

def usd():
   global entrada
   global simbolo

   if (entrada == ''):
      entrada = 'USD'
      button_us.configure(height=20)
      button_us.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)

   elif (entrada == 'USD'):
      entrada = ''
      button_us.configure(height=30)
      button_us.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

   else:
      simbolo = 'US$'
      converta('USD')

def eur():
   global simbolo
   global entrada


   if (entrada == ''):
      entrada = 'EUR'
      button_eur.configure(height=20)
      button_eur.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)

   elif (entrada == 'EUR'):
      entrada = ''
      button_eur.configure(height=30)
      button_eur.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

   else:
      simbolo = '€'
      converta('EUR')


def lib():
   global simbolo
   global entrada

   if (entrada == ''):
      entrada = 'GBP'
      button_lib.configure(height=20)
      button_lib.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)

   elif (entrada == 'GBP'):
      entrada = ''
      button_lib.configure(height=30)
      button_lib.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)

   else:
      simbolo = '£'
      converta('GBP')

def jp():
   global simbolo
   global entrada

   if (entrada == ''):
      entrada = 'JPY'
      button_jp.configure(height=20)
      button_jp.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)

   elif (entrada == 'JPY'):
      entrada = ''
      button_jp.configure(height=30)
      button_jp.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)

   else:
      simbolo = '¥'
      converta('JPY')



def converta(moeda):
   global entrada
   valor = str(caixa_texto.get())
   valor = valor.replace(',','.')
   valor = float(valor)
   conversor = Converter(valor)
   conversor.utilizando_cotacao(moeda, entrada)
   exibir(conversor)


def exibir(conversor):
   resultado = simbolo + " " + str(conversor.valor_convertido)
   texto.configure(text=resultado, )



#Imagem:
my_img = customtkinter.CTkImage(light_image=Image.open('../src/assets/capa.jpg'), size=(200, 200))
my_label = customtkinter.CTkLabel(janela, text="", image=my_img)
my_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
my_label.pack(padx=10, pady=15)


#Criando a caixa de input
caixa_texto = customtkinter.CTkEntry(janela, placeholder_text="Digite aqui")
caixa_texto.pack(padx=10, pady=10, )


#altera a posição do objeto
caixa_texto.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

#Criando o texto onde vai constar o valor convertido
texto = customtkinter.CTkLabel(janela, text="US$ 0.00")
texto.pack(padx = 10, pady = 10)
texto.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)



#botao Dólar

button_us = customtkinter.CTkButton(janela, text="US$", command=usd, height=30, width=30, border_width=0, corner_radius=10)
button_us.pack(padx = 10, pady= 10)
button_us.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

# Botão Euro

button_eur = customtkinter.CTkButton(janela, text="€", command=eur, height=30, width=30, border_width=0, corner_radius=10)
button_eur.pack(padx = 10, pady= 10)
button_eur.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)


# Botão Libra

button_lib = customtkinter.CTkButton(janela, text='£', command=lib, height=30, width=30, border_width=0, corner_radius=10 )
button_lib.pack(padx =5, pady=5)
button_lib.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)

# Botão Real

button_real = customtkinter.CTkButton(janela, text='R$', command=brl, height=30, width=30, border_width=0, corner_radius=10 )
button_real.pack(padx =5, pady=5)
button_real.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)

# Botão Iene

button_jp = customtkinter.CTkButton(janela, text='¥', command=jp, height=30, width=30, border_width=0, corner_radius=10 )
button_jp.pack(padx =5, pady=5)
button_jp.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)





janela.mainloop()
