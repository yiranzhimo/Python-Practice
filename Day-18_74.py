import random
lis = list()
for i in range(1,1002):
    if i % 5 == 0 and i % 7 == 0 :
        lis.append(str(i))
print(random.sample(lis,5))