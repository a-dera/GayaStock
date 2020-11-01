'''
Menu Navigation
'''
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList


from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


KV = '''
#les items du menu
<ItemDrawer>:
    theme_text_color:'Custom'
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id:icon
        icon:root.icon
        theme_text_color:'Custom'
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding:'8dp'
    spacing:'8dp'

    AnchorLayout:
        anchor_x: 'left'
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: '56dp', '56dp'
            source:'img/github.png'
        
    MDLabel:
        text: 'Gaya Stock'
        font_style:'Button'
        size_hint_y: None
        height: self.texture_size[1]
    
    MDLabel:
        text: 'Application de gestion de sctok'
        font_style:'Caption'
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list

Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: "vertical"

                    MDToolbar:
                        title: "Application de gestion de stock"
                        elevation: 10
                        left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        right_action_items:[["dots-vertical", lambda x: x]]

                    Widget:


                    MDLabel:
                        text: "Bienvenue"
                        halign:"center"
                    
                    MDCard: 
                        orientation: "vertical"
                        padding:"8dp"
                        size_hint:None,None
                        size:"280dp","180dp"
                        pos_hint:{'center_x':.2,'center_y':.2}

                        MDLabel:
                            text:'Nombre de ventes de la journées'
                            theme_text_color:'Secondary'
                            size_hint_y:None
                            height: self.texture_size[1]

                        MDSeparator:
                            height:"1dp"
                        
                        MDLabel:
                            text:'Texte texte texte texte texte texte texte texte texte texte'
                        
                    MDCard: 
                        orientation: "vertical"
                        padding:"8dp"
                        size_hint:None,None
                        size:"280dp","180dp"
                        pos_hint:{'center_x':.2,'center_y':.2}

                        MDLabel:
                            text:'Nombre de ventes de la journées'
                            theme_text_color:'Secondary'
                            size_hint_y:None
                            height: self.texture_size[1]

                        MDSeparator:
                            height:"1dp"
                        
                        MDLabel:
                            text:'Texte texte texte texte texte texte texte texte texte texte'


                    

                    MDCard: 
                        orientation: "vertical"
                        padding:"8dp"
                        size_hint:None,None
                        size:"280dp","180dp"
                        pos_hint:{'center_x':.2,'center_y':.2}

                        MDLabel:
                            text:'Nombre de ventes de la journées'
                            theme_text_color:'Secondary'
                            size_hint_y:None
                            height: self.texture_size[1]

                        MDSeparator:
                            height:"1dp"
                        
                        MDLabel:
                            text:'Texte texte texte texte texte texte texte texte texte texte'
                        
                    #pour les tests de direction, les slides
                    MDRectangleFlatButton:
                        text:"Créer un compte"
                        pos_hint:{'center_x':.6,'center_y':.5}
                        on_press:
                            root.manager.transition.direction = "left"
                            root.addbtn()

                    
                    
                    #a mettre a la fin, a la fin, je dis bien a la fin
                    MDFloatingActionButtonSpeedDial:
                        data: app.data
                        rotation_root_button: True

        
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

    
    


       
            
'''
kvi = '''
BoxLayout:
    orientation: "vertical"

    MDLabel:
        text:'Mot de pass ou identifiant incorrect'
        halign:"center"
            
'''

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Renvoyer lorsqu'on clique sur un item du menu'''

        #couleur icon et text pour les items
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class TestNavigationDrawer(MDApp):
    data = {
        'redo': 'Nouvelle vente',
        'undo': 'Nouvelle livraison',
    }
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        # if test()==True:#connexion établie avec l'utilisateur
        return Builder.load_string(KV)
        # else:
        #     return Builder.load_string(kvi)
    
    def on_start(self):
        icons_item = {
            "home":"Accueil",
            "folder":"Catalogue",
            "file":"Fiches",
            "bank":"Tresorerie",
            "history":"Activité",
            "graph":"Statistiques",
            "repeat":"Contact",
            "settings":"Options",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

    def addbtn(self):#juste pour les tests de directions, les slides
        return Builder.load_string(kvi)
            

    
TestNavigationDrawer().run()