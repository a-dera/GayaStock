#expsion panel
from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
Screen:

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
'''



class Test(MDApp):
    data = {
        'in': 'Nouvelle vente',
        'back': 'Nouvelle livraison',
    }
    def build(self):
        return Builder.load_string(KV)
    
Test().run()