'''simple boutonn'''

from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

class getinApp(MDApp):
    '''
    C'est la classe qui gère la création de compte et la connexion
    '''
    def build(self):
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text = "Application de gestion de cave",
                pos_hint = {"center_x":0.5, "center_y":0.5},
            )
        )
        return screen
        
    
getinApp().run()