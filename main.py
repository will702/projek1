from kivymd.app import MDApp
from kivy.lang import Builder

from function.config import Config
import os
from string import  ascii_lowercase
from random import randint ,choice

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






        self.screen = Builder.load_file(self.config.screen)

        return self.screen





 
    picture = 'kbw.png'

    def change_handwriting_to_text(self):
        from google.cloud import vision
        import io
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

        client = vision.ImageAnnotatorClient()

        with io.open(self.picture, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.document_text_detection(image=image)

        for page in response.full_text_annotation.pages:
            for block in page.blocks:


                for paragraph in block.paragraphs:

                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols
                        ])

                        self.screen.nav_layout.screen_manager.screen1.isi.text = word_text



        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))












if __name__ == '__main__':
    OneApp().run()

