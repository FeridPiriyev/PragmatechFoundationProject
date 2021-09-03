## Algorithms


- Verilən str="""Proqramlaşdırma nə qədər çox şey
bildiyinizlə yox, bildiyinizlə ortaya
çıxardığınız işlərlə maraqlanır
"""


### 1.str daxilində neçə xarakter var
```
print(len(str))
```


### 2.str daxilinde herflerin sayi
```
bosluq= " "
bosluqSayi=0
for xarakter in str:
    if xarakter==bosluq:
        bosluqSayi+=1

print(len(str)-bosluqSayi)
```

### 3.str daxilindeki sozleri ayri massivde yaz
```
 bosluq= " "
bosluqSayi=0
for xarakter in str:
    if xarakter==bosluq:
        bosluqSayi+=1

sozlereBolunmusCumle=str.split(" ")
print(sozlereBolunmusCumle)
```

### 4.str daxilinde nece sait samit oldugunu tap
```
saitler=["a","i","u","o","ə","e","ı"]
saitSayi=0
for herf in str:
    for sait in saitler:
        if herf==sait:
            saitSayi+=1
print(saitSayi)
```

print(saitSayi)



### 5.2 string halına gətir
```
str="Proqramlaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır"
ayirma=str.split(",")

print(ayirma)
```


### 6.stringSearch
```
def stringSearch(_word):
    if _word in str:
        print(f"{_word} sozu verilen cumlede movcuddur")
    else:
            print(f"{_word} sozu verilen cumlede movcud deyil")
```

### 7.Ədədlərin cəmi
```
nums=[1,2,3,6,7,8,23,78,34,12]
sum=0
for eded in nums:
    sum+=eded
print(sum)
```

### 8. Böyükdən kiçiyə
```
nums=[1,2,3,6,7,8,23,78,34,12]

nums.sort(reverse=True)
print(nums)
```

### 9. Reqemlerinin cemi en boyuk
```
nums=[1,2,3,6,7,8,23,78,34,12,43]
reqemCemiMassivi=[]
for num in nums:
    sum=0
    for h in str(num):
        sum+=int(h)
    reqemCemiMassivi.append(sum)
```

### 10.Ədədlərin kvadratı

```
nums=[1,2,3,6,7,8,23,78,34,12]
numsKvadrat=[]
for eded in nums:
    numsKvadrat.append(eded**2)


print(numsKvadrat)
```
### 11. Tək ədədlər

```
nums = [1,2,3,6,7,8,23,78,34,12]
tekolan=[]
for tek in nums:
    if tek%2!=0:
        tekolan.append(tek)
print(tekolan)
```

### 12.https://www.hackerrank.com/challenges/py-hello-world/problem
```
print "Hello, World!"
```


### 13.https://www.hackerrank.com/challenges/py-if-else/problem
```
n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
```
### 14. https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
```
a = int(raw_input())
b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)
```

### 15.https://www.hackerrank.com/challenges/python-division/problem
```
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
```

### 16. https://www.hackerrank.com/challenges/python-print/problem
```
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
for i in range (n):
    print(i+1,end="")
```



