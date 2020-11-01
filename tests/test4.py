#botom
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Application de gestion de cave"
        icon:"plus"
        type:"bottom"
        left_action_items:[["menu", lambda x: x]]
'''


class Test(MDApp):
    '''
    le toolbar
    '''
    def build(self):
        return Builder.load_string(KV)
        
    
Test().run()