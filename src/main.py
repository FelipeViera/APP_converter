from classes import Converter
import flet as ft


def main(pagina: ft.Page):
    pagina.title = "Converter Moeda"

    pagina.window_height = 450
    pagina.window_width = 450
    
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.bgcolor = "white"

    def enviar(e):
        valor = float(caixa_texto.value)
        conversor = Converter(valor)
        conversor.utilizando_cotacao()
        resultado.value = "U$ " + str(conversor.valor_convertido)
        pagina.update()



    #Criando a caixa de texto

    botao_ok = ft.IconButton(ft.icons.ADD, on_click= enviar)
    caixa_texto = ft.TextField(value="0", width=100, text_align= ft.TextAlign.CENTER, color="black")
    texto = ft.Text(value="Digite aqui: ", size=35, text_align= ft.TextAlign.CENTER, color="black")
    resultado = ft.Text(value="U$ 0,00", size=35, text_align= ft.TextAlign.CENTER, color="black")
    pagina.add(
        ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([caixa_texto, botao_ok], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([resultado], alignment=ft.MainAxisAlignment.CENTER),
    )

    
    

ft.app(target=main)

