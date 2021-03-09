import numpy

C = 50
H = 30

str = input("请输入想要计算的数字：")
num = str.split(",")

for i in num:
    x = numpy.sqrt((2*C*int(i))/H)
    print(int(x))