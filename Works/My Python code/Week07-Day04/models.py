  
class User:
    def __init__(self,_ad,_soyad,_email,_tel):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.tel=_tel
    def showUserData(self):
        print(f'{self.ad} | {self.soyad} | {self.email} | {self.tel}')
    
users=[]