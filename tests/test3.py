'''menu a gauhe et dot a droite'''
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "test delay"
    MDBottomAppBar:

        MDToolbar:
            id:check
            icon:'plus'
            type:'bottom'
            mode:'free-end'
            md_lg_color:app.theme_cls.accent_color
            # on_release: app.t()
            # active: check.on_release()
            active:app.t()
    Screen:
        MDSpinner:
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x':.5,'center_y':.6}
            delay:0.2
            active: True if check.active else False

        MDCheckbox:
            id:check_spin
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x':.5,'center_y':.4}
            active: False
'''


class Test(MDApp):
    '''
    le toolbar
    '''
    def t(self):
        active=True
        return active

    def build(self):
        return Builder.load_string(KV)
    
Test().run()