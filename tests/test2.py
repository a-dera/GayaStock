'''box'''
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Créer un nouveau compte"

    MDLabel:
        text: "création d'un nouveau compte"
        halign:"center"
'''


class Test(MDApp):
    '''
    le toolbar
    '''
    def build(self):
        return Builder.load_string(KV)
        
    
Test().run()