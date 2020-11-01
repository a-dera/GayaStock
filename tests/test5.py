#expsion panel
from kivy.lang import Builder

from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd import images_path

KV = '''
<Content>
    adaptive_height: True

<Content1>
    adaptive_height: True
    orientation:'vertical'

    OneLineIconListItem:
        text: "Nouvelle Livraison"

        IconLeftWidget:
            icon:'undo'
    
    OneLineIconListItem:
        text: "Nouvelle Livraison"

        IconLeftWidget:
            icon:'undo'

    OneLineIconListItem:
        text: "Nouvelle Vente"
        on_release:app.tes()

        IconLeftWidget:
            icon:'redo'

ScrollView:
    GridLayout:
        id:box
        cols:1
        adaptive_height: True

'''


class Content(BoxLayout):
    '''Custom content'''

class Content1(BoxLayout):
    '''Custom content'''

class Test(MDApp):
    '''
    '''
    def tes(self):
        self.root.ids.box.add_widget(
            MDExpansionPanel(
                icon=f"{images_path}kivymd_logo.png",
                content=Content1(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Catalogue",
                )
            )
        )
    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        self.root.ids.box.add_widget(
            MDExpansionPanel(
                icon=f"{images_path}kivymd_logo.png",
                content=Content(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Accueil",
                )
            )
        )

        self.root.ids.box.add_widget(
            MDExpansionPanel(
                icon=f"{images_path}kivymd_logo.png",
                content=Content1(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Catalogue",
                )
            )
        )
        
    
Test().run()