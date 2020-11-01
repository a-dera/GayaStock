#expsion panel
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
FloatLayout:

    MDFlatButton:
        text:"ALERT DIALOG"
        pos_hint:{'center_x':.5,'center_y':.5}
        on_release:app.show_alert_dialog()
'''



class Test(MDApp):
    '''
    '''
    dialog=None
    def build(self):
        return Builder.load_string(KV)
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL"
                    ),
                    MDFlatButton(
                        text="DISCARD"
                    ),
                ],
            )
        self.dialog.open()
    
        
    
Test().run()