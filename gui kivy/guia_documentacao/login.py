from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginTela(GridLayout):
    def __init__(self, **kwargs):
        super(LoginTela, self).__init__(**kwargs)
        self.cols= 2
        self.add_widget(Label(text='Usuário'))
        self.nomeUsuario= TextInput(multiline=False)
        self.add_widget(self.nomeUsuario)

        self.add_widget(Label(text='senha'))
        self.senha= TextInput(password=True, multiline=False)
        self.add_widget(self.senha)

class LoginApp(App):
    def build(self):
        return LoginTela()
    
if __name__ == '__main__':
    LoginApp().run()