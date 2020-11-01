
from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
Screen:

    MDCard: 
        orientation: "vertical"
        padding:"8dp"
        size_hint:None,None
        size:"280dp","180dp"
        pos_hint:{'center_x':.5,'center_y':.5}

        MDLabel:
            text:'Title'
            theme_text_color:'Secondary'
            size_hint_y:None
            height: self.texture_size[1]

        MDSeparator:
            height:"1dp"
        
        MDLabel:
            text:'Body'

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
   
Test().run()