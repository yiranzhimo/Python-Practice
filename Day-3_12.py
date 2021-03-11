lis = list()
for i in range(1000,3031):
    if i % 2 == 0:
        lis.append(str(i))
str = " ".join(lis)
print(str)