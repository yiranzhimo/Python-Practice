import random
lis = list()
for i in range(0,11):
    if i % 2 == 0:
        lis.append(i)
print(random.choice(lis))
#random.choice从序列中获取一个随机元素