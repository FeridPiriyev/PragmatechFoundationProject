  
from models import *
import json
id=1;
def addUser():
    while True:
        global id
        ad=input('Ad : ')
        soyad=input('Soyad : ')
        email=input('Email : ')
        tel=input('Telefon : ')
        user=User(id,ad,soyad,email,tel)
        users.append(user.__dict__)
        id+=1
        file=open("sample.json","w")
        userJson=json.dumps(users)
        file.write(userJson)
        emr=input('Yeni telebe etmek isteyirsiniz mi? (Y/N) :')
        if emr=='N':
            break
    
def showAllUsers():
    f=open('sample.json','r')
    dataFromJson=f.read()
    convertJsonToDict=json.loads(dataFromJson)
    for n in convertJsonToDict:
        print(f'Istifadecinin adi {n["ad"]} | Istifadecinin soyadi : {n["soyad"]}')
        
def deleteUser():

    silinecekId=int(input("Silmek istediyiniz istifadecinin idsini daxil edin :"))
    f=open('sample.json','r')
    dataFromJson=f.read()
    convertJsonToDict=json.loads(dataFromJson)
    for n in convertJsonToDict:
        if n["id"]==silinecekId:
            convertJsonToDict.remove(n)
    file=open("sample.json","w")
    userJson=json.dumps(convertJsonToDict)
    file.write(userJson)


def updateUser():
    deyisdirilecekId=int(input("Deyisdirmek istediyiniz istifadecinin id-sini daxil edin :"))
    f=open('sample.json','r')
    dataFromJson=f.read()
    convertJsonToDict=json.loads(dataFromJson)
    for n in convertJsonToDict:
        if n["id"]==deyisdirilecekId:
            ad=input("Yeni adı daxil edin :")
            n["ad"]=ad
    file=open("sample.json","w")
    userJson=json.dumps(convertJsonToDict)
    file.write(userJson)