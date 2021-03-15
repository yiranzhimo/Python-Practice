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


