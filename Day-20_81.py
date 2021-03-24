lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in lis:
    if i%5 != 0 and i%7 != 0:
        lis_new.append(i)
print(lis_new)
#for循环按照索引值读取