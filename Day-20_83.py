lis = [12,24,35,70,88,120,155]
lis_new = list()
for i in range(len(lis)):
    if i < 2 or i > 4:
        lis_new.append(lis[i])
print(lis_new)
