from kivymd.uix.screen import  MDScreen
from kivmob import KivMob
class Screen2(MDScreen):
    ads = KivMob('ca-app-pub-1818238534900904~2025018602')# ADS ID 


    ads.new_interstitial('ca-app-pub-1818238534900904/8138357580')#ADS UNIT ID
    ads.add_test_device('7569F1B8DC0951A')#Test Device ID 
    ads.request_interstitial()


    def resume(self):
        self.ads.request_interstitial()

    def show_ads(self):
        self.ads.show_interstitial()
