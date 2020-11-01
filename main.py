
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.config import Config 
Config.set('graphics', 'resizable','0')
Config.set('graphics', 'width','100')
Config.set('graphics', 'height','100')

from datetime import datetime
from  activation_code_decode import decode
from user_test import test_user
import sqlite3
from inscription import insert
from time_fill import dtx

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MyLayout(BoxLayout):
    scr_mngr=ObjectProperty(None)
    dialog=None

    def check_data_login(self):
        premier_caract = self.scr_mngr.activationscreen.premier_caract.text
        quatre_caract = self.scr_mngr.activationscreen.quatre_caract.text
        deux_lettres = self.scr_mngr.activationscreen.deux_lettres.text
        deux_chiffres = self.scr_mngr.activationscreen.deux_chiffres.text
        deux_lettres_last = self.scr_mngr.activationscreen.deux_lettres_last.text


        premier_caract = int(premier_caract)
        quatre_caract = int(quatre_caract)
        deux_lettres = str(deux_lettres)
        deux_chiffres = int(deux_chiffres)
        deux_lettres_last = str(deux_lettres_last)

        code = decode(premier_caract,quatre_caract,deux_lettres,deux_chiffres,deux_lettres_last)
        
        if code == True:
            self.change_screen("connexionscreen")
            # self.change_screen("mainscreen")

        else:#faire a paraitre un popup
            def inv(self):
        
                pop = Popup(
                    title='Erreur', 
                    content=Label(text="Le code d'activiation est invalide!"), 
                    size_hint=(None, None), 
                    size=(400, 400)
                )

                pop.open()
            inv(self)
    
    def xyz(self): 
        self.change_screen("mainscreen") 
            
    def check_user_info(self):
        identifiant = self.scr_mngr.conscreen.identifiant.text
        mdp = self.scr_mngr.conscreen.mdp.text

        identifiant = str(identifiant)
        mdp = str(mdp)

        temp = test_user(identifiant,mdp)


        if temp == 'True':
            self.change_screen("mainscreen")

        else:#faire a paraitre un popup
            def inv(self):
        
                pop = Popup(
                    title='Erreur', 
                    content=Label(text="Le mot de passe ou l'identifiant est incorect"), 
                    size_hint=(None, None), 
                    size=(400, 400)
                )

                pop.open()
            inv(self)

    def save_user_info(self):
        nom = self.scr_mngr.insscreen.nom.text
        prenom = self.scr_mngr.insscreen.prenom.text
        tel = self.scr_mngr.insscreen.tel.text
        mail = self.scr_mngr.insscreen.mail.text
        id_ins = self.scr_mngr.insscreen.id_ins.text
        mdp_ins = self.scr_mngr.insscreen.mdp_ins.text
        confmdp = self.scr_mngr.insscreen.confmdp.text


        nom = str(nom)
        prenom = str(prenom)
        tel = str(tel)
        mail = str(mail)
        id_ins = str(id_ins)
        mdp_ins = str(mdp_ins)
        confmdp = str(confmdp)

        dt = datetime.now()
        dtx = dt.strftime("%d/%m/%Y %H:%M:%S")
        dtx = str(dtx)

        print(mdp_ins)
        print(confmdp)
        print(confmdp==mdp_ins)

        if confmdp != mdp_ins:
            def inv(self):
            
                pop = Popup(
                    title='Erreur', 
                    content=Label(text="Le mot de passe de confirmation est différent"), 
                    size_hint=(None, None), 
                    size=(400, 400)
                )

                pop.open()
            inv(self)


        elif insert(nom,prenom,id_ins,mdp_ins,tel,mail,dtx) == True:
            self.change_screen("mainscreen")

        else:#faire a paraitre un popup
            def inv(self):
        
                pop = Popup(
                    title='Erreur', 
                    content=Label(text="Erreur inconnue durant la connexion à la base de donnée. Recommencez"), 
                    size_hint=(None, None), 
                    size=(400, 400)
                )

                pop.open()
            inv(self)

    def change_screen(self,screen,*args):
        self.scr_mngr.current = screen

    def change_screen2(self,screen,*args):
        self.main_scr_mngr.current = screen
    
    def callback(self,instance):
        if instance.icon=='undo':
            self.change_screen2('livraisonscreen')
        elif instance.icon=='redo':
            self.change_screen2('ventescreen')

KV = '''
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
MyLayout:
    scr_mngr:scr_mngr
    main_scr_mngr:main_scr_mngr
    orientation:'vertical'

    ScreenManager:
        id:scr_mngr
        activationscreen:activationscreen
        connexionscreen:connexionscreen
        conscreen:conscreen
        insscreen:insscreen
        mainscreen:mainscreen

        Screen:
            id:activationscreen
            name:'activationscreen'
            premier_caract:premier_caract
            quatre_caract:quatre_caract
            deux_lettres:deux_lettres
            deux_chiffres:deux_chiffres
            deux_lettres_last:deux_lettres_last

            BoxLayout:
                orientation: "vertical"
                

                FloatLayout:
                    MDCard: 
                        orientation: "vertical"
                        padding:"8dp"
                        size_hint:None,None
                        size:"480dp","380dp"
                        pos_hint:{'center_x':.5,'center_y':.5}

                        MDLabel:
                            text: "Entrer le code de validation"
                            secondary_text:"Respecter les instructions"
                            theme_text_color:'Primary'
                            pos_hint:{'center_y':.95}
                            halign:'center'
                        
                        MDSeparator:
                            height:"5dp"

                        MDTextField:
                            id:premier_caract
                            hint_text: "Le premier caractère (chiffre)"
                            pos_hint:{'center_y':.9}
                        
                        MDTextField:
                            id:quatre_caract
                            hint_text: "Les 4 caractères suivants (chiffre)"
                            pos_hint:{'center_y':.8}

                        MDTextField:
                            id:deux_lettres
                            hint_text: "Les deux lettres "
                            pos_hint:{'center_y':.7}

                        MDTextField:
                            id:deux_chiffres
                            hint_text: "Les 2 chiffres suivants"
                            pos_hint:{'center_y':.6}

                        MDTextField:
                            id:deux_lettres_last
                            hint_text: "Les 2 dernières lettres "
                            pos_hint:{'center_y':.5}

                        MDRectangleFlatButton:
                            text: "Valider "
                            pos_hint:{'center_x':.5}
                            # on_release:root.check_data_login()
                            on_release:root.xyz()


        Screen:
            id:connexionscreen
            name:'connexionscreen'
                
            FloatLayout:

                MDRoundFlatButton:
                    text:"Se connecter"
                    pos_hint:{'center_x':.4,'center_y':.5}
                    on_release:root.change_screen('conscreen')

                MDRoundFlatButton:
                    text:"Créer un compte"
                    pos_hint:{'center_x':.6,'center_y':.5}
                    on_release:root.change_screen('insscreen')

        Screen:
            id:conscreen
            name:'conscreen'
            identifiant:identifiant
            mdp:mdp

                

            FloatLayout:
                MDCard: 
                    orientation: "vertical"
                    padding:"8dp"
                    size_hint:None,None
                    size:"380dp","280dp"
                    pos_hint:{'center_x':.5,'center_y':.5}

                    MDLabel:
                        text: "Entrer vos informations"
                        theme_text_color:'Primary'
                        pos_hint:{'center_y':.95}
                        halign:'center'
                    
                    MDSeparator:
                        height:"5dp"

                    MDTextField:
                        id:identifiant
                        hint_text: "Identifiant"
                        pos_hint:{'center_y':.9}
                    
                    MDTextField:
                        id:mdp
                        hint_text: "Mot de passe"
                        pos_hint:{'center_y':.8}
                        password:True

                    MDRectangleFlatButton:
                        text: "Valider "
                        pos_hint:{'center_x':.5}
                        on_release:root.check_user_info()


        Screen:
            id:insscreen
            name:'insscreen'
            nom:nom
            prenom:prenom
            tel:tel
            mail:mail
            id_ins:id_ins
            mdp_ins:mdp_ins
            confmdp:confmdp


            FloatLayout:
                MDCard: 
                    orientation: "vertical"
                    padding:"8dp"
                    size_hint:None,None
                    size:"480dp","640dp"
                    pos_hint:{'center_x':.5,'center_y':.5}

                    MDLabel:
                        text: "Entrer vos informations"
                        secondary_text: 'création de compte'
                        theme_text_color:'Primary'
                        pos_hint:{'center_y':.9}
                        halign:'center'
                    
                    MDSeparator:
                        height:"5dp"
                    
                    MDTextField:
                        id:nom
                        hint_text: "Nom"
                        pos_hint:{'center_y':.7}
                    
                    MDTextField:
                        id:prenom
                        hint_text: "Prenom"
                        pos_hint:{'center_y':.6}
                    
                    MDTextField:
                        id:tel
                        hint_text: "Téléphone"
                        pos_hint:{'center_y':.5}
                    
                    MDTextField:
                        id:mail
                        hint_text: "Email"
                        pos_hint:{'center_y':.4}
                    
                    MDTextField:
                        id:id_ins
                        hint_text: "Identifiant"
                        pos_hint:{'center_y':.3}
                    
                    MDTextField:
                        id:mdp_ins
                        hint_text: "Mot de passe"
                        pos_hint:{'center_y':.2}
                        password:True

                    MDTextField:
                        id:confmdp
                        hint_text: "Confirmation du mot de passe"
                        pos_hint:{'center_y':.1}
                        password:True


                    MDRectangleFlatButton:
                        text: "Valider "
                        pos_hint:{'center_x':.5}
                        on_release:root.save_user_info()

        # écran principale
        Screen:
            id:mainscreen
            name:'mainscreen'

            NavigationLayout:

                ScreenManager:
                    id:main_scr_mngr
                    mainscreen:mainscreen
                    # les vues de --->> catalogue
                    livraisonscreen:livraisonscreen
                    ventescreen:ventescreen
                    newunitscreen:newunitscreen
                    modifunitscreen:modifunitscreen
                    supunitscreen:supunitscreen
                    newcatscreen:newcatscreen
                    modifcatscreen:modifunitscreen
                    supcatscreen:supcatscreen
                    # les vues pour la facturation, après une livraison et une vente
                        #les pages de facturations
                    pagefactachatscreen:pagefactachatscreen
                    pagefactventescreen:pagefactventescreen
                        #les pages avec un simple bouton imprimer(dans un joli card)
                    factachatscreen:factachatscreen
                    factventescreen:factventescreen
                    # les vues de --->> fiches
                        #pour les listes
                    allprodscreen:allprodscreen
                    allcatscreen:allcatscreen
                    allfactscreen:allfactscreen
                        #pour les items individuels
                    consproscreen:consprodscreen
                    consfactscreen:consfactscreen
                    oneprodscreen:oneprodscreen
                    onefactscreen:onefactscreen
                    #les vues pour la tresorerie
                    fluxscreen:fluxscreen
                    bilanscreen:bilanscreen
                    #les vues des activités
                    mouvstockscreen:mouvstockscreen
                    #les vues contacts
                    clientscreen:clientscreen
                    oneclientscreen:oneclientscreen
                    addfourscreen:addfourscreen
                    allfourscreen:allfourscreen
                    #les vues options
                    changeidscreen:changeidscreen
                    changemdpscreen:changemdpscreen
                    #les vues stats
                    etatcaissescreen:etatcaissescreen
                    etatstockscreen:etatstockscreen
                    compachatscreen:compachatscreen
                    compventescreen:compventescreen
                    compachatdispscreen:compachatdispscreen
                    compventedispcreen:compventedispscreen
                    



                    Screen:
                        id:mainscreen
                        name:'mainscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Accueil"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["power", lambda x: root.change_screen('conscreen')]]

                            Widget:

                            # FloatLayout:

                            
                            MDCard: 
                                orientation: "vertical"
                                padding:"8dp"
                                size_hint:None,None
                                size:"280dp","180dp"
                                pos_hint:{'center_x':.2,'center_y':.8}

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
                                    text: 'Texte texte texte texte texte texte texte texte texte texte'


                            

                            MDCard: 
                                orientation: "vertical"
                                padding:"8dp"
                                size_hint:None,None
                                size:"480dp","280dp"
                                pos_hint:{'center_x':.6,'center_y':.4}

                                MDLabel:
                                    text:'Etat du Stock'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    height: self.texture_size[1]

                                MDSeparator:
                                    height:"1dp"
                                
                                MDLabel:
                                    text:'un pie graph pour display le x articles vendus et le x livraiison(articles achété)'

                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('livraisonscreen')
                    
                    
                            #a mettre a la fin, a la fin, je dis bien a la fin
                            MDFloatingActionButtonSpeedDial:
                                data: app.data
                                rotation_root_button: True
                                callback:root.callback
                                
                    #place des screen intermédiaires
                    Screen:
                        id:livraisonscreen
                        name:'livraisonscreen'
                        select_prod:select_prod
                        quant_liv:quant_liv
                        info_four:info_four

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Enregistrer une nouvelle Livraison"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDCard: 
                                    orientation: "vertical"
                                    padding:"8dp"
                                    size_hint:None,None
                                    size:"480dp","280dp"
                                    pos_hint:{'center_x':.5,'center_y':.9}

                                    MDLabel:
                                        text:'Nouvelle Livraison'
                                        pos_hint:{'center_x':.5}
                                        halign:'center'

                                    MDSeparator:
                                        height:"1dp"
                                    
                                    MDLabel:
                                        text: 'Faites attention lors du remplissage'
                                        halign:'center'
                                    
                                    MDTextField:
                                        id:select_prod
                                        hint_text: "Selectionner le produit"
                                        pos_hint:{'center_y':.3}

                                    MDTextField:
                                        id:quant_liv
                                        hint_text: "Quantité de livraison"
                                        pos_hint:{'center_y':.3}

                                    MDTextField:
                                        id:info_four
                                        hint_text: "Infos fournisseur"
                                        pos_hint:{'center_y':.3}


                                    MDRectangleFlatButton:
                                        text: "Valider cette livraison"
                                        pos_hint:{'center_x':.5}
                                        on_release:root.change_screen2('pagefactachatscreen')

                    Screen:
                        id:pagefactachatscreen
                        name:'pagefactachatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Page de facturation d'achat(Livraison)"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle Livraison'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5, 'center_y':.5}
                                    height: self.texture_size[1]

                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5, 'center_y':.5}
                                    on_release:root.change_screen2('factachatscreen')

                    Screen:
                        id:factachatscreen
                        name:'factachatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Facture d'achat"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle Livraison'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5, 'center_y':.5}
                                    height: self.texture_size[1]

                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('ventescreen')

                    Screen:
                        id:ventescreen
                        name:'ventescreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Enregistrer une nouvelle Vente"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDCard: 
                                    orientation: "vertical"
                                    padding:"8dp"
                                    size_hint:None,None
                                    size:"480dp","280dp"
                                    pos_hint:{'center_x':.5,'center_y':.9}

                                    MDLabel:
                                        text:'Nouvelle Vente'
                                        pos_hint:{'center_x':.5}
                                        halign:'center'

                                    MDSeparator:
                                        height:"1dp"
                                    
                                    MDLabel:
                                        text: 'Faites attention lors du remplissage'
                                        halign:'center'
                                    
                                    MDTextField:
                                        id:select_prod
                                        hint_text: "Selectionner le produit"
                                        pos_hint:{'center_y':.3}

                                    MDTextField:
                                        id:quant_liv
                                        hint_text: "Quantité de vente"
                                        pos_hint:{'center_y':.3}


                                    MDRectangleFlatButton:
                                        text: "Valider cette vente"
                                        pos_hint:{'center_x':.5}
                                        on_release:root.change_screen2('pagefactventescreen')

                    Screen:
                        id:pagefactventescreen
                        name:'pagefactventescreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Page de facturation de vente"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle Livraison'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5, 'center_y':.5}
                                    height: self.texture_size[1]

                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5,'center_y':.5}
                                    on_release:root.change_screen2('factventescreen')

                    Screen:
                        id:factventescreen
                        name:'factventescreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Facture de vente"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle Livraison'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5,'center_y':.5}
                                    height: self.texture_size[1]

                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5,'center_y':.5}
                                    on_release:root.change_screen2('newunitscreen')

                    Screen:
                        id:newunitscreen
                        name:'newunitscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Enregistrer une toute nouvelle Unité de produits dans votre Stock"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5,'center_y':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5,'center_y':.5}
                                    on_release:root.change_screen2('modifunitscreen')

                    Screen:
                        id:modifunitscreen
                        name:'modifunitscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Modifier les données d'une unité de produit"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('supunitscreen')

                    Screen:
                        id:supunitscreen
                        name:'supunitscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Supprimer une unité de produit"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('newcatscreen')

                    Screen:
                        id:newcatscreen
                        name:'newcatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Enregistrer une nouvelle Catégorie"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDCard: 
                                    orientation: "vertical"
                                    padding:"8dp"
                                    size_hint:None,None
                                    size:"380dp","280dp"
                                    pos_hint:{'center_x':.5,'center_y':.5}

                                    MDLabel:
                                        text: "Les données de la nouvelle catégorie"
                                        theme_text_color:'Primary'
                                        pos_hint:{'center_y':.95}
                                        halign:'center'
                                    
                                    MDSeparator:
                                        height:"5dp"

                                    MDTextField:
                                        id:lib_cat
                                        hint_text: "Libellé de la catégorie"
                                        pos_hint:{'center_y':.8}

                                    
                                    MDTextField:
                                        id:desc_cat
                                        hint_text: "Description"
                                        pos_hint:{'center_y':.7}

                                    MDRectangleFlatButton:
                                        text: "Valider "
                                        pos_hint:{'center_x':.5}
                                        on_release:root.change_screen2('modifcatscreen')



                    Screen:
                        id:modifcatscreen
                        name:'modifcatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Modifier une Catégorie"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('supcatscreen')

                    Screen:
                        id:supcatscreen
                        name:'supcatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Supprimer une Catégorie"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('allprodscreen')

                    #screens des fiches à suivre
                    Screen:
                        id:allprodscreen
                        name:'allprodscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "La liste de tous les produits en Stock"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('allcatscreen')

                    Screen:
                        id:allcatscreen
                        name:'allcatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "La liste de toutes les catégories enregistrées"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('allfactscreen')

                    Screen:
                        id:allfactscreen
                        name:'allfactscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "La liste de toutes les factures générées"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('consprodscreen')
                    
                    Screen:
                        id:consprodscreen
                        name:'consprodscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Rechercher et visualiser les détails d'un produit"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('oneprodscreen')
                    
                    Screen:
                        id:oneprodscreen
                        name:'oneprodscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Détails sur le produit"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('consfactscreen')

                    Screen:
                        id:consfactscreen
                        name:'consfactscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Rechercher et visualiser les détails d'une facture"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('onefactscreen')

                    Screen:
                        id:onefactscreen
                        name:'onefactscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Détails sur la facture"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('fluxscreen')

                    #screen tresorerie à suivre
                    Screen:
                        id:fluxscreen
                        name:'fluxscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Flux de la caisse"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('bilanscreen')
                    Screen:
                        id:bilanscreen
                        name:'bilanscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Votre Bilan Comptable"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('mouvstockscreen')
                    #screen activité
                    Screen:
                        id:mouvstockscreen
                        name:'mouvstockscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Mouvements du Stock"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:
                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('clientscreen')

                    #screen contact
                    Screen:
                        id:clientscreen
                        name:'clientscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Fiches sur les clients"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('oneclientscreen')
                    
                    Screen:
                        id:oneclientscreen
                        name:'oneclientscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Détails sur un client"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            MDLabel:
                                text:'Nouvelle vente'
                                theme_text_color:'Secondary'
                                size_hint_y:None
                                pos_hint:{'center_x':.5}
                                height: self.texture_size[1]


                            MDRectangleFlatButton:
                                text: "Valider"
                                pos_hint:{'center_x':.5}
                                on_release:root.change_screen2('addfourscreen')
                    
                    Screen:
                        id:addfourscreen
                        name:'addfourscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Ajouter un nouveau fournisseur"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('allfourscreen')
                    
                    Screen:
                        id:allfourscreen
                        name:'allfourscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Fiches sur les fournisseurs"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('changeidscreen')

                    #screen options
                    Screen:
                        id:changeidscreen
                        name:'changeidscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Changer votre identifiant de connexion"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('changemdpscreen')
                    
                    Screen:
                        id:changemdpscreen
                        name:'changemdpscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Changer votre mot de passe de connexion"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('etatcaissescreen')

                    #screen stats
                    Screen:
                        id:etatcaissescreen
                        name:'etatcaissescreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Etat de la Caisse"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('etatstockscreen')
                    
                    Screen:
                        id:etatstockscreen
                        name:'etatstockscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Etat de votre Stock"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('compachatscreen')
                    
                    Screen:
                        id:compachatscreen
                        name:'compachatscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Choisissez deux produits pour comparer leur livraison"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('compachatdispscreen')
                    Screen:
                        id:compachatdispscreen
                        name:'compachatdispscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Résultats de la comparaison de livraison"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('compventescreen')

                    Screen:
                        id:compventescreen
                        name:'compventescreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Choisissez deux produits pour comparer leur vente"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('compventedispscreen')
                    
                    Screen:
                        id:compventedispscreen
                        name:'compventedispscreen'

                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Résultats de la comparaison de vente"
                                elevation: 10
                                left_action_items:[["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                                right_action_items:[["home", lambda x: root.change_screen2('mainscreen')]]

                            Widget:

                            FloatLayout:

                                MDLabel:
                                    text:'Nouvelle vente'
                                    theme_text_color:'Secondary'
                                    size_hint_y:None
                                    pos_hint:{'center_x':.5}
                                    height: self.texture_size[1]


                                MDRectangleFlatButton:
                                    text: "Valider"
                                    pos_hint:{'center_x':.5}
                                    on_release:root.change_screen2('mainscreen')






                
                MDNavigationDrawer:
                    id: nav_drawer

                    ContentNavigationDrawer:
                        id: content_drawer


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


class GayaStock(MDApp):
        
    title ='Gaya Stock'

    dialog=None

    data = {
        'redo': 'Nouvelle vente',
        'undo': 'Nouvelle livraison',
    }

    def build(self):
        return Builder.load_string(KV) 

    def on_start(self):
        icons_item = {
            "home":"**ACCUEIL**",
            "none":"------------------------------------",
            "folder":"**CATALOGUE**",
            "none1":"------------------------------------",
            "file":"**FICHES**",
            "none2":"------------------------------------",
            "bank":"**TRESORERIE & COMPTABILITE**",
            "none3":"------------------------------------",
            "history":"**ACTIVITE**",
            "none4":"------------------------------------",
            "graph":"**STATISTIQUES**",
            "none5":"------------------------------------",
            "repeat":"**CONTACT**",
            "none6":"------------------------------------",
            "settings":"**OPTIONS**",
            "none7":"------------------------------------",
            "account-circle-outline":"Amédée",
            "alert-circle-outline":"DERA",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            ),
            if icon_name=='folder':
                icons = {
                    "undo":"Nouvelle Livraison",
                    "redo":"Nouvelle Vente",
                    "file":"Nouvelle Unité",
                    "pencil":"Modifier une unité",
                }
                for icon_nam in icons.keys():
                    self.root.ids.content_drawer.ids.md_list.add_widget(
                        ItemDrawer(icon=icon_nam, text=icons[icon_nam])
                    )   

          
GayaStock().run()