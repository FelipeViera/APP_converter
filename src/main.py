
from classes import Converter
import flet as ft



def main(pagina: ft.Page):
    pagina.title = "Converter Moeda"

    pagina.window_height = 450
    pagina.window_min_height = 450
    pagina.window_max_height = 450
    pagina.window_min_width = 450
    pagina.window_max_width = 450
    pagina.window_width = 450
    
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.bgcolor = "white"


    def enviar(e):
        valor = caixa_texto.value
        valor = valor.replace(',','.')
        valor = float(valor)
        conversor = Converter(valor)
        conversor.utilizando_cotacao()
        resultado.value = "U$ " + str(conversor.valor_convertido)
        resultado.color = "green"
        pagina.update()



    #Criando a caixa de texto

    botao_ok = ft.IconButton(ft.icons.ROTATE_LEFT, on_click= enviar,height=100, width=100, icon_size=45)
    caixa_texto = ft.TextField(value="0", width=100, text_align= ft.TextAlign.CENTER, color="black")
    descripe = ft.Text(value="Converta Real em Dólar", size=30, text_align= ft.TextAlign.CENTER, color="black")
    texto = ft.Text(value="Digite aqui: ", size=25, text_align= ft.TextAlign.CENTER, color="black",)
    resultado = ft.Text(value="U$ 0,00", size=35, text_align= ft.TextAlign.CENTER, color="black")
    
    pagina.add(

        ft.Row(
            [ft.Container(
                content = descripe   

            )], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Container(
                content= texto,
                margin =10
            )
        ], alignment=ft.MainAxisAlignment.CENTER),
            
        ft.Row([ft.Container(
            content = caixa_texto,
            margin = ft.margin.Margin(155, 0, 30, 0)
            
            

        ), botao_ok], alignment=ft.MainAxisAlignment.CENTER),
        
        ft.Row([resultado], alignment=ft.MainAxisAlignment.CENTER)
    )

    
    

ft.app(target=main)

