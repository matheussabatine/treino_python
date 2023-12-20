from kivy.app import App
from kivy.uix.label import Label

class Calculadora(App):
    def build(self):
        return Label(text='Bom dia')
    
if __name__ == '__main__':
    Calculadora().run()