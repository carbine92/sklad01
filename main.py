from kivymd.app import MDApp

from kivymd.uix.floatlayout import MDFloatLayout

class Container(MDFloatLayout):
    pass
class Sklad(MDApp):
    def build(self):
        return Container()


Sklad().run()