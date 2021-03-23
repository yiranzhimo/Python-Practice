import random
lis = list()
for i in range(0,151):
    if i % 5 == 0 and i % 7 == 0 :
        lis.append(str(i))
print(random.choice(lis))