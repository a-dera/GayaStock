'''
Projet de test 
'''
from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='hello world', font_size='50sp')

HelloApp().run()