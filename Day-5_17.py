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
        

