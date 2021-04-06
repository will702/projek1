#Kivy Import
from kivymd.uix.button import MDRaisedButton,MDFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

#Python Import
from . import nulis
import glob
import os
from google_trans_new import google_translator
#Layout Import
from  . screen2 import Screen2
from . navigationlayout import NavigationLayout

class ScreenLayout(FloatLayout):
    try:
        #Put Screen2 On Main Layout
        Screen2()
        #Nav Bar Layout
        NavigationLayout()





        def check_data_login(self):
            try:
                self.get_permission()
                try:





                    nama = self.nav_layout.screen_manager.screen1.username.text

                    kelas = self.nav_layout.screen_manager.screen1.kelas.text
                    font = self.nav_layout.screen_manager.screen1.spinn.text
                    kertas = self.nav_layout.screen_manager.screen1.spinn1.text

                    isi = self.nav_layout.screen_manager.screen1.isi.text

                    prs = nulis.Fung(isi, kertas, font, nama, kelas)
                    prs.textNulis()

                    self.nav_layout.screen_manager.screen2.image1.source = prs.return_location()
                    self.change_screen('screen2')

                except:
                    pass
            except:
                pass


        def translation(self):
            try:
                self.get_permission()
                try:
                    translator = google_translator()
                    translate_text = translator.translate(self.nav_layout.screen_manager.screen1.isi.text, lang_src='id',
                                                          lang_tgt='en')

                    self.nav_layout.screen_manager.screen1.isi.text = translate_text
                except:
                    pass
            except:
                pass

        def see_recent_images(self):
            try:
                self.get_permission()
                try:

                    self.list_of_files = glob.glob(f'{os.getcwd()}/TypeToWritePhotos/*.png')  # * means all if need specific format then *.csv
                    self.latest_file = max(self.list_of_files, key=os.path.getctime)
                    self.nav_layout.screen_manager.screen2.image1.source = self.latest_file

                except:
                    pass
            except:
                pass

        def search_kertas(self):
            try:
                if self.nav_layout.screen_manager.screen3.spinn12.text == '1':
                    self.nav_layout.screen_manager.screen2.image1.source  = 'bahan/bahan_1.jpg'
                    self.see_kertas10()

                if self.nav_layout.screen_manager.screen3.spinn12.text == '2':
                    self.nav_layout.screen_manager.screen2.image1.source = 'bahan/bahan_2(1).jpg'
                    self.see_kertas10()
                if self.nav_layout.screen_manager.screen3.spinn12.text == '3':
                    self.nav_layout.screen_manager.screen2.image1.source = 'bahan/bahan_3.jpg'
                    self.see_kertas10()
                if self.nav_layout.screen_manager.screen3.spinn12.text == '4':
                    self.nav_layout.screen_manager.screen2.image1.source = 'bahan/bahan_4.jpg'
                    self.see_kertas10()
                if self.nav_layout.screen_manager.screen3.spinn12.text == '5':
                    self.nav_layout.screen_manager.screen2.image1.source = 'bahan/bahan_5.jpg'
                    self.see_kertas10()
            except:
                pass

        def get_permission(self):
            try:
                if platform == 'android':
                    from android.permissions import Permission, request_permissions
                    def callback(permission, results):
                        if all([res for res in results]):
                            pass
                        else:
                            pass

                    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE,Permission.CAMERA], callback)
            except:
                pass
        def see_kertas10(self):
            try:
                self.change_screen("screen2")
            except:
                pass

        def see_kertas(self):
            try:
                self.change_screen("screen3")
            except:
                pass


        def back(self):
            try:
                self.change_screen("screen1")
            except:
                pass
        def show_dialog(self):
            try:
                self.dialog = MDDialog(title='warning', text='Are you sure to log out',
                                       size_hint=(0.5, 1),
                                       buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)
                                           , MDRaisedButton(text='Sign Out', on_release=self.sign_out)])

                self.dialog.open()
            except :
                pass

        def close_dialog(self, obj):
            try:
                self.dialog.dismiss()
            except:
                pass

        def change_screen(self, screen, *args):
            try:
                self.nav_layout.screen_manager.current = screen
            except:
                pass

        def sign_out(self, obj):
            try:
                self.nav_layout.screen_manager.firebase_login_screen.log_out()
                self.change_screen('firebase_login_screen')
            except:
                pass
    except:
        pass