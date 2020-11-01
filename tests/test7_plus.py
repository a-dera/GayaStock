'''le bouton plus en bas a droie en mode free-end'''
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:


    MDBottomAppBar:

        MDToolbar:
            title: "Application de gestion de cave"
            icon:'plus'
            type:'bottom'
            left_action_items:[["menu", lambda x: x]]
            mode:'free-end'


            
'''


class Test(MDApp):
    '''
    le toolbar
    '''
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
        
    
Test().run()