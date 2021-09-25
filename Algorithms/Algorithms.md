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

```    print("Not Weird")
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


### 17. https://www.hackerrank.com/challenges/python-loops/problem
```
if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(0,n):
        print(i*i)
```

### 18. https://www.hackerrank.com/challenges/write-a-function/problem
```
def is_leap(a):
    if a %400==0:
        return True
    if a%100==0:
        return False
    if a%4==0:
        return True
    return False
    
    
    
    
year = int(input())
print(is_leap(year))
```

### 19. https://www.hackerrank.com/challenges/solve-me-first/problem
```
def solveMeFirst(a,b):
	return a+b


a = input()
b = input()
res = solveMeFirst(a,b)
print res
```

### 20. https://www.hackerrank.com/challenges/js10-hello-world/problem
```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   A line of code that prints "Hello, World!" on a new line is provided in the editor. 
*   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
*
*	Parameter:
*   parameterVariable - A string of text.
**/
function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');

    // Write a line of code that prints parameterVariable to stdout using console.log:
    console.log(parameterVariable);
}


function main() {
    const parameterVariable = readLine();
    
    greeting(parameterVariable);
}
```

### 21.https://www.hackerrank.com/challenges/30-hello-world/problem

```
function processData(inputString) {
    // This line of code prints the first line of output
    console.log("Hello, World.");
    
    // Write the second line of output that prints the contents of 'inputString' here.
    console.log(inputString)
}


process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
```

### 22.Siyahıdakı ədədlərin cəmi (8, 2, 3, 0, 7)
```
nums=[8, 2, 3, 0, 7]
sum=0
for eded in nums:
    sum+=eded
print(sum)
```

### 22.Siyahıdakı ədədlərin hasili (8, 2, 3, -1, 7)
```
def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x
    return result
     
list1 = [8, 2, 3, -1, 7]
print(multiplyList(list1))
```

### 24.Siyahıdakı elementlərin sonuncusu
```
test_list = [1,24,26,17,76,9]
  
# printing original list 
print ("The original list is : " + str(test_list))
  
for i in range(0, len(test_list)):
  
if i == (len(test_list)-1):
    print ("The last element of list using loop : "
+ str(test_list[i]))
```

### 25. Siyahıdakı cüt ədədlər
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cutolan=[]
for cut in nums:
    if cut%2==0:
        cutolan.append(cut)
print(cutolan)
```

### 26.Daxil olunan bütün ədədlər toplansın
```
sum=0
nocount=0

while True:
    number=float(input("Enter the number :"))
    sum += number
    nocount += 1


    choice=input("Add another number? (y/n)")
    if choice.casefold() == "n":
        break



print(f"sum : {sum}")
```

### 27.https://www.hackerrank.com/challenges/js10-if-else/problem
```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    if(score>25 && score<=30) grade='A';
    else if(score>20 && score<=25) grade='B';
    else if(score>15 && score<=20) grade='C';
    else if(score>10 && score<=15) grade='D';
    else if(score>5 && score<=10) grade='E';
    else if(score>0 && score<=5) grade='F';
    
    return grade;
}


function main() {
    const score = +(readLine());
    
    console.log(getGrade(score));
}
```

### 28.https://www.hackerrank.com/challenges/js10-data-types/problem
```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/**
*   The variables 'firstInteger', 'firstDecimal', and 'firstString' are declared for you -- do not modify them.
*   Print three lines:
*   1. The sum of 'firstInteger' and the Number representation of 'secondInteger'.
*   2. The sum of 'firstDecimal' and the Number representation of 'secondDecimal'.
*   3. The concatenation of 'firstString' and 'secondString' ('firstString' must be first).
*
*    Parameter(s):
*   secondInteger - The string representation of an integer.
*   secondDecimal - The string representation of a floating-point number.
*   secondString - A string consisting of one or more space-separated words.
**/
function performOperation(secondInteger, secondDecimal, secondString) {
    // Declare a variable named 'firstInteger' and initialize with integer value 4.
    const firstInteger = 4;
    console.log(firstInteger+Number(secondInteger));
    
    // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
    const firstDecimal = 4.0;
     console.log(firstDecimal+Number(secondDecimal));
    
    // Declare a variable named 'firstString' and initialize with the string "HackerRank".
    const firstString = 'HackerRank ';
    console.log(firstString+String(secondString));
    
    // Write code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to a Number        type) on a new line.
    
    
    // Write code that uses console.log to print the sum of 'firstDecimal' and 'secondDecimal' (converted to a Number            type) on a new line.
    
    
    // Write code that uses console.log to print the concatenation of 'firstString' and 'secondString' on a new line. The        variable 'firstString' must be printed first.
    
}

```

### 29. https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem
```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;
    // Write your code here
    area=length*width
    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*	
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    // Write your code here
    perimeter=(length+width)*2
    return perimeter;
}


function main() {
    const length = +(readLine());
    const width = +(readLine());
    
    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}
```

### 30. https://www.hackerrank.com/challenges/js10-function/problem
```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */
function factorial(number){
let fact=1;
for(let i=1;i<=number;i++){
fact*=i;
}
return fact;
}

function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}
```

### 31. 


