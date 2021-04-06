from . screenlayout import ScreenLayout


from  . contentnavigationdrawer import ContentNavigationDrawer,ItemDrawer

class Config:
    def __init__(self):
        self.title = 'Type To Write'
        self.color  = 'LightBlue'
        self.screen = 'layout/screenlayout.kv'
        self.id_key = "AIzaSyBmrGpiwimYZ-HT_BSesv4gMjuPJcG3omM"

        ScreenLayout()
        ContentNavigationDrawer()
        ItemDrawer()

        