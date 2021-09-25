ad=input("Adınız:")
soyad=input("Soyadınız:")

adSoyad=f"{ad} / {soyad}\n"
file=open("data.txt","a")
file.write(adSoyad)