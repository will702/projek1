from kivymd.app import MDApp
from kivy.lang import Builder

from function.config import Config
from google.cloud import storage
from kivy.network.urlrequest import UrlRequest
import certifi
from kivy.clock import  mainthread

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


            """Uploads a file to the bucke-server-teset."""
            bucket_name = 'typetowritebucket'
            destination_blob_name = "test-storage-blob.png"
            debug = True

            if not debug == True:
                storage_client = storage.Client()
            else:
                cred_file = 'ServiceAccountToken.json'
                storage_client = storage.Client.from_service_account_json(cred_file)

            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(self.picture)
            print(
                "File {} uploaded to {}.".format(
                    self.picture, destination_blob_name
                )
            )

            self.hit_cloud_function(destination_blob_name)


        except:
            pass

    @mainthread
    def hit_cloud_function(self, blob_name):

        from urllib.parse import urlencode
        msg_data = urlencode({'message': blob_name})
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}

        trigger_url = "https://us-central1-type-to-write.cloudfunctions.net/function-1"
        UrlRequest(trigger_url, req_body=msg_data, req_headers=headers, ca_file=certifi.where(),
                   on_failure=self.error, on_error=self.error, on_success=self.success)

    def error(self, *args):
        self.screen.nav_layout.screen_manager.screen1.isi.text = str(f'error{args}')
    def success(self, request, response):

        print("Success!")
        print(response)
        self.screen.nav_layout.screen_manager.screen1.isi.text = response
        self.screen.change_screen('screen1')


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





 


















if __name__ == '__main__':
    OneApp().run()

