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