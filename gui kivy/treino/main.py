from kivy.app import App
from kivy.lang import Builder
import requests

GUI= Builder.load_file('tela.kv')

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    # funções que acontecem ao abrir o app
    def on_start(self):
        #root se refere ao arquivo kv carregado no builder (neste caso tela.kv)
        self.root.ids['caso1'].text= f"Dólar $$$: {self.pega_cotacao('USD')}"
        self.root.ids['caso2'].text= f"Euro $$$: {self.pega_cotacao('EUR')}"

    def pega_cotacao(self, moeda):
        link= f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao= requests.get(link)
        dic_requisicao= requisicao.json()
        cotacao= dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
    
if __name__ == '__main__':
    MeuAplicativo().run()