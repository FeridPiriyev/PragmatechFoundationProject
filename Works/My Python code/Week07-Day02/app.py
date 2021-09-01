def  Foo(_ad,_soyad="Kerimov"):
    print(f"{_ad}-{_soyad}")

#Foo("Samir")
#Foo("Kenan","Rizvanlı")


def Bar(_ad,*args):
    print(_ad,args)

Bar(2,3,56,42,50)
