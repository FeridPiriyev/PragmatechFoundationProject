from functions import *
import os
while True:
    print("""
    -------------------------------------------------------------------
    Möhtəşəm proqramın möhtəşəm menyusu
    - Yeni istifadəçi əlavə etmək üçün 1 düyməsinə basın
    - Bütün istifadəçiləri görə bilmək üçün 2 düyməsinə basın
    - İstifadəçi silmək üçün 3 düyməsinə basın
    - İstifadəçi məlumatlarını dəyişmək üçün 4 düyməsinə basın
    - Proqramdan çıxmaq üçün 5 düyməsinə basın
    -------------------------------------------------------------------
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