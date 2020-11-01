'''le bouton plus en bas a droie en mode free-end'''
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

KV = '''
FloatLayout:


    MDContextMenu:
        menu:app.menu
        pos_hint:{'top':1}
        on_enter:app.on_enter(*args)

        MDContextMenuItem:
            text:'File'

        MDContextMenuItem:
            text:'Edit'

        

            
'''

MENU = [
    [
        'File', [
            {'Item 1':[]}, {
                'Item 2':[
                    'Item 1',
                    'Separator',
                    ['language-python','Item 3'],
                ]
            },
            'Separator',
            {'Item 3':[]},
        ],
    ],
    [
        'Edit',
        ['language-swift','Item 1']
    ]
]

class Test(MDApp):
    context_menu = None
    menu = MENU 

    def on_enter(self, instance):
        print(instance.current_selected_menu.text)
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
        
    
Test().run()