# Python-Practice
Python 练习题，[题目来源](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended)。

## Day 1

> 1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
list=[]
for i in range(2000,3001):
    if i%7==0 and i%5 !=0:
        list.append(i)
print(list)
```
> 2.Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

```python
num=int(input("请输入数字："))
i=0
j=1
while i<num:
    j=(i+1)*j
    i=i+1
print(j)
```

> 3.With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

```python
num=int(input("请输入您的数字："))
dic=dict()
if num<=0:
    print("输入不规范！")
for i in range(1,num+1):
    if i>0:
        dic[i]=i*i
print(dic)
```


## Day2

> 4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

```python
num = input("请输入您想要的数字：")
num = num.split(",")
print(num)
#列表生成
tup1 = tuple(num)
print(tup1)
#元组转换成列表

```

> 5.Define a class which has at least two methods: getString: to get a string from console input,printString: to print the string in upper case. Also please include simple test function to test the class methods.
```python
class myclass():
    def getString(self):
        self.s = input("请输入：")
    def printString(self):
        print(self.s.upper())
test = myclass()
test.getString()
test.printString()
```

> 6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

```python
import numpy

C = 50
H = 30

str = input("请输入想要计算的数字：")
num = str.split(",")

for i in num:
    x = numpy.sqrt((2*C*int(i))/H)
    print(int(x))
```

> 7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
```
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

**第 7 题不明白意思，遂弃**

> 8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
```
without,hello,bag,world
```
> Then, the output should be:
```
bag,hello,without,world
```

```python
text = input("请输入 words:")
lis = text.split(",")
lis.sort()
str = " ".join(lis)
print(str)
```

> 9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
```
Hello world
Practice makes perfect
Then, the output should be:
```
```
HELLO WORLD
PRACTICE MAKES PERFECT
```

```python
lines=[]
while True:
    try:
        lines.append(input())
    except:
        break

for i in lines:
    print(i.upper())
```

## Day3

> 10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

> Suppose the following input is supplied to the program:

```
hello world and practice makes perfect and hello world again
```

> Then, the output should be:

```
again and hello makes perfect practice world
```

```python
words = input("请输入 words:")
words_new = words.split(" ")
words_result = list()
for i in words_new:
    if i not in words_result:
        words_result.append(i)
words_result.sort()
str = " ".join(words_result)
print(str)    
```

>11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
>Example:
```
0100,0011,1010,1001
```
>Then the output should be:
```
1010
```

```python
nums = input("请输入二进制数字：").split(",")
lis = list()
for item in nums:
    item_new = int(item,2)
    if item_new % 5 == 0:
        print(item)
```

> 12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
lis = list()
for i in range(1000,3031):
    if i % 2 == 0:
        lis.append(str(i))
str = " ".join(lis)
print(str)
```

> 13.Write a program that accepts a sentence and calculate the number of letters and digits.

> Suppose the following input is supplied to the program:
```
hello world! 123
```
> Then, the output should be:
```
LETTERS 10
DIGITS 3
```

```python
import re
words = input("请输入 words:")
letters_result = ' '.join(re.findall(r'[A-Za-z]', words)).split()
list(letters_result)
digit_result = ' '.join(re.findall(r'[0-9]+', words)).split()
list(digit_result)
print("LETTERS ",len(letters_result))
print("DIGITS ",len(digit_result))
```
## Day4

> 14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

> Suppose the following input is supplied to the program:
```
Hello world!
```
> Then, the output should be:
```
UPPER CASE 1
LOWER CASE 9
```
```python
import re
word = input("请输入 words:")
result = ' '.join(re.findall(r'[A-Za-z]', word)).split()
list(result)
i = 0 
j = 0
for item in result:
    if item.islower() is True:
        i = i + 1
    else:
        j = j + 1
print("UPPER CASE ",j)
print("LOWER CASE ",i)

#使用了 re 模块的 findall 函数找到字母。
```

> 14.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
> Suppose the following input is supplied to the program:
```
9
```
> Then, the output should be:
```
11106
```
```python
def Plu(num):
    num = str(input("请输入数字："))
    x1 = num * 1
    x2 = num * 2
    x3 = num * 3
    x4 = num * 4 
    Num = int(x1) + int(x2) + int(x3) + int(x4)
    print(Num)
Plu(9)
```
## Day5

> 16.Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
```
1,2,3,4,5,6,7,8,9
```

> Then, the output should be:

```
1,9,25,49,81
```
```python
nums = input("请输入 nums：").split(",")
nums = list(map(int,nums))
lis = list()
for item in nums:
    if item % 2 != 0:
        lis.append(item**2)
print(lis)

#运用 map 函数把 list 中国的字符串转换为 int
```
> 17.Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
```
D 100
W 200
```
> D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
```
D 300
D 300
W 200
D 100
```
> Then, the output should be:
```
500
```
```python
import re
lines = list()
while True:
    try:
        lines.append(input())
    except:
        break
#实现多行输入
lis_1 = list()
lis_2 = list()
for i in lines:
    if "D" in i:
        nums = re.findall('[0-9]',i)
        num = int("".join(nums))
        lis_1.append(num)
    else:
        nums = re.findall('[0-9]',i)
        num = int("".join(nums))
        lis_2.append(num)
print(sum(lis_1)-sum(lis_2))
```

## Day6

> 18.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

> Following are the criteria for checking the password:
```
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
```
> Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

> Example

> If the following passwords are given as input to the program:
```
ABd1234@1,a F1#,2w3E*,2We3345
```

> Then, the output of the program should be:
```
ABd1234@1
```
```python
import re
passwords = input("请输入密码：").split(",")
for item in passwords:
    i = 0
    j = 0
    l = 0
    m = 0
    for word in item:
        if re.match(r"\d",word):
            i = i + 1
            #数字计数
        elif re.match("[a-z]",word):
            j = j + 1
        elif re.match("[A-Z]",word):
            l = l + 1
        elif re.match("[$#@]",word):
            m = m + 1
                
    
    if i >=1 and j >=1 and l >= 1 and m >=1 and len(item) in range(6,13):
        print(item)
```

> 19.You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
* 1: Sort based on name
* 2: Then sort based on age
* 3: Then sort by score
> The priority is that name > age > score.
> If the following tuples are given as input to the program:
```
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
```
> Then, the output of the program should be:
```
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```
```python
lines = list()
lis = list()
while True:
    try:
        lines.append(input())
    except:
        break
#多行输入
for i in range(0,len(lines)):
    lis.append(tuple(lines[i].split(",")))
print(sorted(lis))
```
> 20.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
> Suppose the following input is supplied to the program:
```
7
```
> Then, the output should be:
```
0
7
14
```
```python
class test():
    def test(self):
        x = int(input("请输入数字:"))
        for i in range(0,20):
            if i%x == 0:
                print(i)
Test = test()
#把类实例化
Test.test()
```
> 21.A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```
> The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```
> Then, the output of the program should be:
```
2
```
```python
import re
import numpy
def test():
#定义开方函数
    lines = list()
    while True:
        try:
            lines.append(input())
        except:
            break
#多行输入
    for item in lines:
        if "UP" in item:
            x = re.findall(r"\d",item)
        elif "DOWN" in item:
            y = re.findall(r"\d",item)
        elif "LEFT" in item:
            l = re.findall(r"\d",item)
        else:
            m = re.findall(r"\d",item)
    a = int(x[0])-int(y[0])
    b = int(l[0])-int(m[0])
    c = a**2 + b**2
#获得最后的值
    print(int(numpy.sqrt(c)))

test()
```
> Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
> Suppose the following input is supplied to the program:
```
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
```
> Then, the output should be:
```
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
```
```python
import re
word = input("请输入字符串：")
words = re.split(r" ",word)
#re.split 可以按照空格划分，而 str.split 直接全部切割
lis = list()
for item in words:
    if item not in lis:
        lis.append(item)
for item in sorted(lis):
    print(item,":",word.count(item))
```

> 23.Write a method which can calculate square value of number

```python
def test():
    num = int(input("请输入数字："))
    print(num**2)
test()
```
> 24.Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

> Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

> And add document for your own function

```python
print(int.__doc__)
def test(num):
    '''
    export half of the number
    '''
    return(num/2)

test(2)
print(test.__doc__)
```

> 25.Define a class, which have a class parameter and have a same instance parameter.

```python
class Fruits:
    name = "Fruits"
    def __init__(self,name = None):
        self.name = name
    
orange = Fruits("Orange")
print("orange name is",orange.name)

grape = Fruits()
grape.name = "Grape"
print("grape name is",grape.name)
#这一题做的不明不白的。
```
> 26.Define a function which can compute the sum of two numbers.
```python
def Add(a,b):
    return(a+b)

print(Add(2,3))
```

> 27.Define a function that can convert a integer into a string and print it in console.

```python
def tra(i):
    return(str(i))

print(tra(3))
```

> 28.Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
```python
def add(a,b):
    return(int(a)+int(b))
print(add("2","3"))
```

> 29.Define a function that can accept two strings as input and concatenate them and then print it in console.
```python
def link(a,b):
    return(a+b)

print(link("hh","biubiu"))
```

> 30.Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
```python
def mor(a,b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    else:
        print(a,b)
mor("hh","biubiu")
```

> 31.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
```python
def test():
    dic = dict() 
    for i in range(1,21):
        dic[i]=i*i
    return dic
print(test())
#此时不需要定义参数
```
> 32.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
```python
def test():
    dic = dict() 
    for i in range(1,21):
        dic[i]=i*i
    return dic.keys()
print(test())
#此时不需要定义参数
```
> 33.Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
```python
def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return lis
print(test())
#此时不需要定义参数
```
> 34.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
```python
def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return lis[0:5]
print(test())
#此时不需要定义参数
```

> 35.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
```python
def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return lis[-5:]
print(test())
#此时不需要定义参数
```
> 36.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
```python
def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return lis[5:]
print(test())
#此时不需要定义参数
```

> 37.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
```python
def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return tuple(lis)
print(test())
```

> 38.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
```python
tuple = (1,2,3,4,5,6,7,8,9,10)
tuple_1 = tuple[0:5]
tuple_2 = tuple[5:10]
print(tuple_1)
print(tuple_2)
```

> 39.Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
```python
tuple_1 = (1,2,3,4,5,6,7,8,9,10)
lis = list()
for i in tuple_1:
    if i%2 ==0:
        lis.append(i)
print(tuple(lis))
```

> 40.Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
```python
X = input("请输入字符串：")
if X.lower() == "yes":
    print("Yes")
else:
    print("No")
```
> 41.Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
```python
def squ(i):
    return i*i

lis_1 = [1,2,3,4,5,6,7,8,9,10]
print(list(map(squ, lis_1)))
```

> 42.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
```python
def even(i):
    return i%2 ==0

def squ(i):
    return i*i

lis = [1,2,3,4,5,6,7,8,9,10]
print(list(map(squ,filter(even,lis) )))
#filter(function, iterable)，function -- 判断函数，iterable -- 可迭代对象。
```

> 43.Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
```python
def even(i):
    return i%2 == 0
lis = list()
for i in range(1,21):
    lis.append(i)
print(list(filter(even,lis)))
```

> 44.Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
```python
def squ(i):
    return i*i

lis = list()
for i in range(1,21):
    lis.append(i)
print(list(map(squ, lis)))
```
> 45.Define a class named American which has a static method called printNationality.
```python
class American():
    def printNationality(self):
        print("Are you American?")

test = American()
test.printNationality()
```
> 46.Define a class named American and its subclass NewYorker.
```python
class American():
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)
```
> 47.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
```python
class Circle():
    def __init__(self,r):
        self.radius = r
    def area(self):
        return(3.14*self.radius*self.radius)
circle = Circle(2)
print(circle.area())
#慢慢了解 self,__init__ 的概念。
```
> 48.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
```python
class Circle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return(self.length*self.width)
circle = Circle(3,4)
print(circle.area())
```

> 49.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
```python
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length*self.length

square = Square(5)
print(square.area())
print(Square().area())
```
> 50.Please raise a RuntimeError exception.
```python
raise RuntimeError('something wrong')
```
> 51.Write a function to compute 5/0 and use try/except to catch the exceptions.
```python
def test():
    return 5/0
try:
    test()
except:
    print("Exception")
```
> 52.Define a custom exception class which takes a string message as attribute.

**第 52 题不明白意思，遂弃**

> 53.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

> Example: If the following email address is given as input to the program:

```john@google.com```
> Then, the output of the program should be:

```john```
```python
import re
str = input("请输入字符串：")
str_new = re.findall(r'(\w*)@',str)
print("".join(str_new))
#()可以表示匹配的范围
```

> 54.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

> Example: If the following email address is given as input to the program:

```john@google.com```
> Then, the output of the program should be:

```google```
> In case of input data being supplied to the question, it should be assumed to be a console input.

```python
import re
str = input("请输入字符串：")
str_new = re.findall(r'\w*@(\w*).',str)
print("".join(str_new))
```
> 55.Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

> Example: If the following words is given as input to the program:

```2 cats and 3 dogs.```
> Then, the output of the program should be:

```['2', '3']```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
import re
str = input("请输入字符串：")
str_new = re.findall(r'(\d)\s\w*',str)
print(str_new)
#这个匹配比较模糊
```
> 56.Print a unicode string "hello world".
```python
unicodeString = u"hello world!"
print(unicodeString)
```
> 57.Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
```python
X = input("请输入 ASCII 编码字符串：")
print(X.encode('utf-8'))
```

> 58.Write a special comment to indicate a Python source code file is in unicode.
```python
# -*- coding: utf-8 -*-
```
> 59.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

> Example: If the following n is given as input to the program:
```
5
```
> Then, the output of the program should be:
```
3.55
```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
N = int(input("请输入数字："))
X = 0 
for i in range(1,N+1):
    X = i/(i+1) + X
print(X)
```

> 60.Write a program to compute:
```
f(n)=f(n-1)+100 when n>0
and f(0)=0
```
> with a given n input by console (n>0).
> Example: If the following n is given as input to the program:
```
5
```
> Then, the output of the program should be:
```
500
```
```python
n = int(input("请输入数字："))
i = 0
j = 0
while i < n:
    i = i + 1
    j = j + 100
print(j)
```
> 61.The Fibonacci Sequence is computed based on the following formula:
```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```
> Please write a program to compute the value of f(n) with a given n input by console.

> Example: If the following n is given as input to the program:
```
7
```
> Then, the output of the program should be:
```
13
```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
n = int(input("请输入数字："))
lis = list()
j = 0
if n == 0:
    print(j)
if n == 1:
    j = j + 1
    print(j)
i = 1
if n > 1:
    lis.append(0)
    lis.append(1)
    while i < n:
        i = i + 1
        j = lis[i-1]+lis[i-2]
        lis.append(j)
    print(lis[i])
```
> 62.The Fibonacci Sequence is computed based on the following formula:
```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```
> Please write a program to compute the value of f(n) with a given n input by console.
> Example: If the following n is given as input to the program:
```
7
```
> Then, the output of the program should be:
```
0,1,1,2,3,5,8,13
```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
n = int(input("请输入数字："))
lis = list()
j = 0
if n == 0:
    print(j)
if n == 1:
    j = j + 1
    print(j)
i = 1
if n > 1:
    lis.append(0)
    lis.append(1)
    while i < n:
        i = i + 1
        j = lis[i-1]+lis[i-2]
        lis.append(j)
    print(lis)
```
> 63.Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
> Example: If the following n is given as input to the program:
```
10
```
> Then, the output of the program should be:
```
0,2,4,6,8,10
```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
n = int(input("请输入数字："))
lis = list()
for i in range(0,n+1):
    if i % 2 == 0:
        lis.append(str(i))
print(",".join(lis))
```
> Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

> Example: If the following n is given as input to the program:
```
100
```
> Then, the output of the program should be:
```
0,35,70
```
> In case of input data being supplied to the question, it should be assumed to be a console input.
```python
n = int(input("请输入数字："))
lis = list()
for i in range(0,n+1):
    if i % 5 == 0 and i % 7 == 0 :
        lis.append(str(i))
print(",".join(lis))
```
> 65.Please write assert statements to verify that every number in the list [2,4,6,8] is even.
```python
lis = [2,4,5,6]
for i in lis:
    assert i%2 == 0
```
> 66.Please write a program which accepts basic mathematic expression from console and print the evaluation result.

> Example: If the following n is given as input to the program:
```
35 + 3
```
> Then, the output of the program should be:
```
38
```
```python
x = input("请输入：")
print(eval(x))
#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
```
> 67.Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
```python
def search(lis,item):
    if item not in lis:
        return None
    if item in lis:
        return lis.index(item)
lis = [1,2,3,4,5]
print(search(lis,3))
```
> 68.Please generate a random float where the value is between 10 and 100 using Python module.
```python
import random
print(random.random()*100)
```
> 69.Please generate a random float where the value is between 5 and 95 using Python module.
```python
import random
print(random.uniform(5, 95))
```
> 70.Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
```python
import random
lis = list()
for i in range(0,11):
    if i % 2 == 0:
        lis.append(i)
print(random.choice(lis))
#random.choice从序列中获取一个随机元素
```

> 71.Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.
```python
import random
lis = list()
for i in range(0,151):
    if i % 5 == 0 and i % 7 == 0 :
        lis.append(str(i))
print(random.choice(lis))
```
> 72.Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
```python
import random
print(random.sample(range(100,201),5))
```
> 73.Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
```python
import random
print(random.sample(range(100,201,2),5))
#range(start, stop, step)
```
> 74.Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
```python
import random
lis = list()
for i in range(1,1002):
    if i % 5 == 0 and i % 7 == 0 :
        lis.append(str(i))
print(random.sample(lis,5))
```
> 75.Please write a program to randomly print a integer number between 7 and 15 inclusive.
```python
import random
print(random.randint(7,16))
#随机整数
```
> 76.Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
```python
import zlib
X = "hello world!hello world!hello world!hello world!"
Y = bytes(X, 'utf-8')
#TypeError: a bytes-like object is required, not 'str'
x = zlib.compress(Y)
print(x)
print(zlib.decompress(x))
```
> 77.Please write a program to print the running time of execution of "1+1" for 100 times.
```python
import time
before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution_time = after - before
print(execution_time)
```
> 78.Please write a program to shuffle and print the list [3,6,7,8].
```python
import random
lis = [1,2,3,4,5,6,7,8,9]
random.shuffle(lis)
print(lis)
#print(random.shuffle(lis))会返回None值
```
> 79.Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
```python
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]
for sub in subjects:
    for verb in verbs:
        for ob in objects:
            item = sub +" "+ verb +" "+ ob
            print(sub +" "+ verb +" "+ ob)
```
> 80.Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
```python
lis = [5,6,77,45,22,12,24]
lis_new = list()
for i in lis:
    if i%2 != 0:
        lis_new.append(i)
print(lis_new)
#for循环按照索引值读取
```

> 81.By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
```python
lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in lis:
    if i%5 != 0 and i%7 != 0:
        lis_new.append(i)
print(lis_new)
#for循环按照索引值读取
```
> 82.By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
```python
lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in range(len(lis)):
    if i != 0 and i !=2 and i !=4 and i !=6:
        lis_new.append(lis[i])
print(lis_new)
```
> 83.By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
```python
lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in range(len(lis)):
    if i < 2 or i > 4:
        lis_new.append(lis[i])
print(lis_new)
```
>84.By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
```python
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```
> 85.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
```python
lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in range(len(lis)):
    if i != 0 and i !=4 and i !=5:
        lis_new.append(lis[i])
print(lis_new)
```
> 86.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
```python
lis = [12,24,35,70,88,120,155]
lis.remove(24)
print(lis)
```
> 87.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
```python
is_1 = [1,3,6,78,35,55]
lis_2 = [12,24,35,24,88,120,155]
print(set.intersection(set(lis_1),set(lis_2)))
#intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
```
> 88.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
```python
l1 = [12,24,35,24,88,120,155,88,120,155]
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
```
> 89.Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
```python
class Person:
    def gender(self):
        return "ALL"


class Male(Person):
    def gender(self):
        return "Male"

class Female(Person):
    def gender(self):
        return "Female"

male = Male()
female = Female()
print(male.gender())
print(female.gender())
```