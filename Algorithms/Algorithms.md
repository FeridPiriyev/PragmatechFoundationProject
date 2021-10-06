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

### 9. Siyahıdakı ədədlərin hasili
```
def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x
    return result
     
list1 = [1,2,3,6,7,8,23,78,34,12]
print(multiplyList(list1))
```

### 10. Reqemlerinin cemi en boyuk
```
nums=[1,2,3,6,7,8,23,78,34,12,43]
reqemCemiMassivi=[]
for num in nums:
    sum=0
    for h in str(num):
        sum+=int(h)
    reqemCemiMassivi.append(sum)
```

### 11.Ədədlərin kvadratı

```
nums=[1,2,3,6,7,8,23,78,34,12]
numsKvadrat=[]
for eded in nums:
    numsKvadrat.append(eded**2)


print(numsKvadrat)
```
### 12. Tək ədədlər

```
nums = [1,2,3,6,7,8,23,78,34,12]
tekolan=[]
for tek in nums:
    if tek%2!=0:
        tekolan.append(tek)
print(tekolan)
```

### 13. Cüt ədədlər
```
nums = [1,2,3,6,7,8,23,78,34,12]
cutolan=[]
for cut in nums:
    if cut%2==0:
        cutolan.append(cut)
print(cutolan)
```

### 14.https://www.hackerrank.com/challenges/py-hello-world/problem
```
print "Hello, World!"
```


### 15.https://www.hackerrank.com/challenges/py-if-else/problem
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
### 16. https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
```
a = int(raw_input())
b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)

```
### 17.https://www.hackerrank.com/challenges/python-division/problem
```
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
```

### 18. https://www.hackerrank.com/challenges/python-print/problem
```
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
for i in range (n):
    print(i+1,end="")
```


### 19. https://www.hackerrank.com/challenges/python-loops/problem
```
if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(0,n):
        print(i*i)
```

### 20. https://www.hackerrank.com/challenges/write-a-function/problem
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

### 21. https://www.hackerrank.com/challenges/solve-me-first/problem
```
def solveMeFirst(a,b):
	return a+b


a = input()
b = input()
res = solveMeFirst(a,b)
print res
```

### 23. https://www.hackerrank.com/challenges/js10-hello-world/problem
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

### 24.https://www.hackerrank.com/challenges/30-hello-world/problem

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

### 25.Siyahıdakı ədədlərin cəmi (8, 2, 3, 0, 7)
```
nums=[8, 2, 3, 0, 7]
sum=0
for eded in nums:
    sum+=eded
print(sum)
```

### 26.Siyahıdakı ədədlərin hasili (8, 2, 3, -1, 7)
```
def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x
    return result
     
list1 = [8, 2, 3, -1, 7]
print(multiplyList(list1))
```

### 27.Siyahıdakı elementlərin sonuncusu
```
test_list = [1,24,26,17,76,9]
  
# printing original list 
print ("The original list is : " + str(test_list))
  
for i in range(0, len(test_list)):
  
if i == (len(test_list)-1):
    print ("The last element of list using loop : "
+ str(test_list[i]))
```

### 28. Siyahıdakı cüt ədədlər
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cutolan=[]
for cut in nums:
    if cut%2==0:
        cutolan.append(cut)
print(cutolan)
```

### 29.Daxil olunan bütün ədədlər toplansın
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

### 30.https://www.hackerrank.com/challenges/js10-if-else/problem
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

### 31.https://www.hackerrank.com/challenges/js10-data-types/problem
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

### 32. https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem
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

### 33. https://www.hackerrank.com/challenges/js10-function/problem
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

### 34. https://www.hackerrank.com/challenges/30-data-types/problem

```
i = 4
d = 4.0
s = 'HackerRank '


input_int=int(input())
input_double=float(input())
input_string=str(input())


print(i+input_int)
print(d+input_double)
print(s+input_string)
```

### 36. https://www.hackerrank.com/challenges/js10-objects/problem

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
function Rectangle(a, b) {
    return {
        length:a,
        width:b,
        perimeter:2*(a+b),
        area:a*b
    }
}
function Rectangle(a, b) {
  this.length = a;
  this.width = b;
  this.area = a * b;
  this.perimeter = 2 * (a + b);
}

function main() {
    const a = +(readLine());
    const b = +(readLine());
    
    const rec = new Rectangle(a, b);
    
    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
```

### 37. https://www.hackerrank.com/challenges/js10-let-and-const/problem
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

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    
    // Print the area of the circle:
    
    // Print the perimeter of the circle:
    const PI=Math.PI;
    let r=readLine();

    var area=parseFloat(PI*r*r);
    console.log(area);
  
    var peri=parseFloat(2*PI*r);
    console.log(peri);
    try {    
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
```

### 38. https://www.hackerrank.com/challenges/js10-switch/problem
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

function getLetter(s) {
    let letter;
    // Write your code here
    
    return letter;
}
function getLetter(s) {
    let letter;
    switch (true) {
        case 'a,e,i,o,u'.includes(s[0]):
            letter = 'A';
            break;
        case 'b,c,d,f,g'.includes(s[0]):
            letter = 'B';
            break;
        case 'h,j,k,l,m'.includes(s[0]):
            letter = 'C';
            break;
        case 'n,p,q,r,s,t,v,w,x,y,z'.includes(s[0]):
            letter = 'D';
            break;
    }
    return letter;
}

function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}
```
### 39. https://www.hackerrank.com/challenges/js10-arrays/problem
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

function getSecondLargest(nums) {
    // Complete the function
   let first = nums[0]; 
   let second = -1;
    for (let i = 0; i < nums.length; i++) {
    if (nums[i] > first) {
        second = first;
        first = nums[i]
    }

    if (nums[i] > second && nums[i] < first) {
        second = nums[i];
    }
}


return second;
}

function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
```

### 40. https://www.hackerrank.com/challenges/js10-throw/problem
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
function isPositive(a) {
    if(a > 0){
        return 'YES';
    }
    else{
        throw (a === 0 ? new Error('Zero Error') : new Error('Negative Error'));
    }
}


```

### 41. https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
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
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    
}
function reverseString(s) {
    try {
        s = s.split('').reverse().join('');
    }
    catch(e) {
        console.log(e.message);
    }
    finally {
        console.log(s);
    }
}

function main() {
    const s = eval(readLine());
    
    reverseString(s);
}
```

### 42. https://www.hackerrank.com/challenges/js10-class/problem
```
/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon{
    constructor(sides){        
        this.sides = sides
    }
    perimeter() {
        return this.sides.reduce(function add(a,b){return a+b;})
    } 
}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
```

### 43. https://www.hackerrank.com/challenges/js10-create-a-button?hr_b=1
## HTML
```
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/button.css" type="text/css">
    </head>
    
    <body>
        <button id="btn" onclick="button()">0</button>
        <script src="js/button.js" type="text/javascript"></script>
    </body>
</html>
```
## CSS
```
#btn {
    width: 96px;
    height: 48px;
    font-size: 24px;
}
```

## JS
```
function button(){
    document.getElementById("btn").innerHTML++;
}
```

### 44. https://www.hackerrank.com/challenges/js10-buttons-container?hr_b=1
## HTML
```
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/buttonsGrid.css" type="text/css">
    </head>
    
    <body>
        
        <div id="btns" class="btnContainer">

            <button id="btn1" class="btnStyle">1</button>

            <button id="btn2" class="btnStyle">2</button>

            <button id="btn3" class="btnStyle">3</button>

            <button id="btn4" class="btnStyle">4</button>

            <button id="btn5" class="btnStyle" onClick="rotate()">5</button>

            <button id="btn6" class="btnStyle">6</button>

            <button id="btn7" class="btnStyle">7</button>

            <button id="btn8" class="btnStyle">8</button>

            <button id="btn9" class="btnStyle">9</button>
        </div>
        <script src="js/buttonsGrid.js" type="text/javascript"></script>
    </body>
</html>
```

## CSS
```
.btnContainer {
width: 75%;
}

.btnContainer > .btnStyle {
width: 30%;
height: 48px;
font-size: 24px;
}
```

## JS
```
  var l = "4";

var a = ["1", "2", "3", "6", "9", "8", "7", "4"];

var b = ["1", "2", "3", "6", "9", "8", "7", "4"];



var rotate = function() {

    for (var i = 7; i > 0; i--) {

        a[i] = a[i - 1];

    }

    a[0] = l;

    l = a[7];

    for (var i = 0; i < 8; i++) {

        document.getElementById("btn" + b[i]).innerText = a[i];

    }

}
```

### 45. https://www.hackerrank.com/challenges/list-comprehensions/problem
```
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
    print(output);
```

### 46. https://www.hackerrank.com/challenges/js10-loops/problem
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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    
}

function vowelsAndConsonants(s) {
  const vowels = ["a", "e", "i", "o", "u"];
  const string = s.split("");
  let vowelArr = [];
  let consonantArr = [];
  for (let i = 0; i < string.length; i++) {
    vowels.includes(string[i])
      ? vowelArr.push(string[i])
      : consonantArr.push(string[i]);
  }
  for (let i = 0; i < vowelArr.length; i++) {
    console.log(vowelArr[i]);
  }
  for (let i = 0; i < consonantArr.length; i++) {
    console.log(consonantArr[i]);
  }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
```

### 47. https://www.hackerrank.com/challenges/js10-count-objects/problem
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
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    
}

function getCount(objects) {
  let pairCount = 0;
  for (let i = 0; i < objects.length; i++) {
    if (objects[i].x === objects[i].y) {
      pairCount++;
    }
  }
  return pairCount;
}


```

### 48. https://www.hackerrank.com/challenges/30-operators/problem

```
import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax
    
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
 
    solve(meal_cost, tip_percent, tax_percent)
```

### 49. https://www.hackerrank.com/challenges/30-conditional-statements/problem
```
import math
import os
import random
import re
import sys




if __name__ == '__main__':
    N = int(input().strip())
    
    if N%2 != 0:
        print("Weird")
    else:
        if N>=2 and N<5:
            print("Not Weird")
    
        if N>=6 and N<=20:
            print("Weird")
    
        if N>20:
            print("Not Weird")
```

### 50. https://www.hackerrank.com/challenges/30-loops/problem
```
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,11):
        s = n * i
        print(n,"x",i,"=",s)

```





