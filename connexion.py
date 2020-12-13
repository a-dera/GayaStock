
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.uix.popup import Popup
from kivy.uix.label import Label

KV = '''
<Content_con>
    orientation:"vertical"
    spacing:"12dp"
    size_hint_y: None
    height:"120dp"

    MDTextField:
        hint_text: "Identifiant"
    
    MDTextField:
        hint_text: "Mot de passe"

<Content_ins>
    orientation:"vertical"
    spacing:"12dp"
    size_hint_y: None
    height:"120dp"

    MDTextField:
        hint_text: "Nom"
    
    MDTextField:
        hint_text: "Prenom"
    
    MDTextField:
        hint_text: "Téléphone"
    
    MDTextField:
        hint_text: "Email"
    
    MDTextField:
        hint_text: "Identifiant"
    
    MDTextField:
        hint_text: "Mot de passe"

    MDTextField:
        hint_text: "Confirmation du mot de passe"
    


FloatLayout:

    MDRectangleFlatButton:
        text:"Se connecter"
        pos_hint:{'center_x':.4,'center_y':.5}
        on_release:app.connexion()
        # on_release:app.inv()

    MDRectangleFlatButton:
        text:"Créer un compte"
        pos_hint:{'center_x':.6,'center_y':.5}
        on_release:app.inscription()
'''

class Content_con(BoxLayout):
    pass


class Content_ins(BoxLayout):
    pass


class Test(MDApp):

    dialog=None

    def build(self):
        return Builder.load_string(KV)

    def connexion(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Connexion",
                type="custom",
                content_cls=Content_con(),
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="VALIDER", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

    def inscription(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Connexion",
                type="custom",
                content_cls=Content_ins(),
                buttons=[
                    MDFlatButton(
                        text="ANNULER", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="VALIDER", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()
    
    def inv(self):

        pop = Popup(
            title='Invalid Form', 
            content=Label(text='Erreur de connexion veuillez vérifier vos identifiants.' ), 
            size_hint=(None, None), 
            size=(400, 400)
        )

        pop.open()
        
    
Test().run()
