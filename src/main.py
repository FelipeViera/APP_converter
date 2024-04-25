from classes import Converter
import flet as ft


def main(pagina: ft.Page):
    pagina.title = "Converter Moeda"

    pagina.window_height = 450
    pagina.window_width = 450
    
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.bgcolor = "white"

    def enviar(e):
        conversor = Converter(100)
        print(conversor.valor)
        conversor.utilizando_cotacao()
        print(conversor.valor_convertido)
        



        
        

    #Criando a caixa de texto

    botao_ok = ft.IconButton(ft.icons.ADD, on_click= enviar)
    caixa_texto = ft.TextField(value="0", width=100, text_align= ft.TextAlign.CENTER, color="black")

    pagina.add(
        ft.Row([caixa_texto, botao_ok], alignment=ft.MainAxisAlignment.CENTER)
    )
    

ft.app(target=main)

