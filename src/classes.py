import requests
import json


class Converter():
    def __init__(self, valor):
        self.valor = valor
        self.valor_convertido = 0
    
  

    def utilizando_cotacao(self, moeda, entrada):
        try:
            link = "https://economia.awesomeapi.com.br/last/" + moeda + "-" + entrada
            cotacoes = requests.get(link)
            cotacoes = cotacoes.json()
            cotacao_moeda = cotacoes[moeda + entrada ]["bid"]
            self.valor_convertido = float(round(self.valor / float(cotacao_moeda), 2))
            
        except:
            print("Erro de conexão")




