def squ(i):
    return i*i

lis = list()
for i in range(1,21):
    lis.append(i)
print(list(map(squ, lis)))