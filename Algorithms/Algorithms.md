## Algorithms


- Verilən str="""Proqramlaşdırma nə qədər çox şey
bildiyinizlə yox, bildiyinizlə ortaya
çıxardığınız işlərlə maraqlanır
"""


### 1.str daxilində neçə xarakter var
 print(len(str))


### 2.str daxilinde herflerin sayi
* bosluq= " "
bosluqSayi=0
for xarakter in str:
    if xarakter==bosluq:
        bosluqSayi+=1

print(len(str)-bosluqSayi)


### 3.str daxilindeki sozleri ayri massivde yaz

* bosluq= " "
bosluqSayi=0
for xarakter in str:
    if xarakter==bosluq:
        bosluqSayi+=1

sozlereBolunmusCumle=str.split(" ")
print(sozlereBolunmusCumle)


### 4.str daxilinde nece sait samit oldugunu tap

"""saitler=["a","i","u","o","ə","e","ı"]
saitSayi=0
for herf in str:
    for sait in saitler:
        if herf==sait:
            saitSayi+=1


print(saitSayi)"""


### 8.Ədədlərin cəmi

nums=[1,2,3,6,7,8,23,78,34,12]
sum=0
for eded in nums:
    sum+=eded
print(sum)