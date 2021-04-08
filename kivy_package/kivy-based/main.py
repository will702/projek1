from kivymd.app import MDApp
from kivy.lang import Builder
from layout.config import Config
from kivmob import KivMob
from string import  ascii_lowercase
from random import randint ,choice
import os

os.environ["KIVY_NO_CONSOLELOG"] = "1"

def randoming_string():
    letters = ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(randint(3, 12)))

    return result_str

class OneApp(MDApp):
    def __init__(self):

        super().__init__()
        

        self.config = Config()

        self.id_key =  self.config.id_key
        self.title = self.config.title
        self.theme_cls.primary_palette = self.config.color

    def picture_taken(self, obj, filename):
        try:

            self.picture = filename
            






        except:
            pass



    def take_picture(self):
        try:
            self.screen.change_screen('camerascreen')
            self.screen.nav_layout.screen_manager.camerascreen.xcamera.restore_orientation()
        except:
            pass
    def build(self):





        self.config = Config()





        self.ads = KivMob('ca-app-pub-1818238534900904~2025018602')
        self.ads.new_banner('ca-app-pub-1818238534900904/4048546717', top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()

        self.screen = Builder.load_file(self.config.screen)

        return self.screen





 


















if __name__ == '__main__':
    OneApp().run()

