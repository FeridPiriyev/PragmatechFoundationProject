class User:
    def __init__(self,_ad,_soyad,__email,__tel):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.tel=_tel
    def showUserData(self):
        print(f'{self.ad} | {self.soyad} | {self.email} | {self.tel}')



def addUser():
    while True:
        ad=input("Ad : ")
        soyad=input("Soyad : ")
        email=input("Email : ")
        tel=input("Telefon : ")
        user=User(ad,soyad,email,tel)
        users.append(user)
        emr=input('Yeni telebe etmek isteyirsiniz mi? (Y/N) :')
        if emr=='N':
            break


def showAllUsers():
    for user in users:
        user.showUserData()

def deleteUser():
    print("Delete User")
def updateUser():
    print("Update User")




while True:
    print("""
-----------------------------------------------------------

Mohtesem saytin mohtesem menyusu
- Yeni istifadəçi əlavə etmək üçün 1 düyməsinə basın
- Bütün istifadəçiləri görə bilmək üçün 2 düyməsinə basın
- İstifadəçi silmək üçün 3 düyməsinə basın
- İstifadəçi məlumatlarını dəyişmək üçün 4 düyməsinə basın
- Proqramdan çıxmaq üçün 5 düyməsinə basın
-----------------------------------------------------------
""")

    order=input('Istədiyiniz əməlyat nömrəsini daxil edin : ')
    if order=='1':
        addUser()
    elif order=='2':
        showAllUsers()
    elif order=='3':
        deleteUser()
    elif order=='4':
        updateUser()
    elif order=='5':
        break
