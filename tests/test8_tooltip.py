'''menu a gauhe et dot a droite'''
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<TooltipMDIconButton@MDIconButton+MDTooltip>

Screen:
    TooltipMDIconButton:
        icon:'language-python'
        tooltip_text:self.icon
        pos_hint:{'center_x':.5,'center_y':.5}
            
'''


class Test(MDApp):
    '''
    le toolbar
    '''
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
        
    
Test().run()