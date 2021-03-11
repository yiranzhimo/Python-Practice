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
