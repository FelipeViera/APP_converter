import requests
import json

class Converter():
    def __init__(self, valor):
        self.valor = valor
        self.valor_convertido = 0
    
  

    def utilizando_cotacao(self):
        try:
            link = "https://economia.awesomeapi.com.br/last/USD-BRL"
            cotacoes = requests.get(link)
            cotacoes = cotacoes.json()
            cotacao_dollar = cotacoes['USDBRL']["bid"]
            self.valor_convertido = float(round(self.valor / float(cotacao_dollar), 2))
            
        except:
            print("errou")




