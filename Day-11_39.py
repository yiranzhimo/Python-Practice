tuple_1 = (1,2,3,4,5,6,7,8,9,10)
lis = list()
for i in tuple_1:
    if i%2 ==0:
        lis.append(i)
print(tuple(lis))

