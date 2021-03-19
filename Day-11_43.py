def even(i):
    return i%2 == 0
lis = list()
for i in range(1,21):
    lis.append(i)
print(list(filter(even,lis)))