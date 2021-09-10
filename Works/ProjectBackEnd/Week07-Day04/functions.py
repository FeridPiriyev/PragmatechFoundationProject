  
from models import *
import json
def addUser():
    while True:
        ad=input('Ad : ')
        soyad=input('Soyad : ')
        email=input('Email : ')
        tel=input('Telefon : ')
        user=User(ad,soyad,email,tel)
        users.append(user)
        file=open("sample.json","w")
        emr=input('Yeni telebe etmek isteyirsiniz mi? (Y/N) :')
        if emr=='N':
            break
    
def showAllUsers():
    for user in users:
        user.showUserData()
def deleteUser():
    print('Delete User')
def updateUser():
    print('Update User')