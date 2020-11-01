'''
Projet de test  MD
'''
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class HelloApp(MDApp):
    def build(self):
        return MDLabel(text='hello world', halign="center")

HelloApp().run()