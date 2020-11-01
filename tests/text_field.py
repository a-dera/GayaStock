
from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
BoxLayout:
    padding:"10dp"

    MDTextField:
        id:text_field_error
        hint_text:"Helper text on error ('press Enter')"
        helper_text:"There will always be mistake"
        helper_text_mode:"on_error"
        pos_hint:{'center_y':.5}


'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
    def build(self):
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen
    
    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True
   
Test().run()