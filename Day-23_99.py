lis_1 = [2,4,5,9]
lis_2 = [2,4,11,12]
lis_1_new = list()
lis_2_new = list()
for i in lis_1:
    if i not in lis_2:
        lis_1_new.append(i)
for i in lis_2:
    if i not in lis_1:
        lis_2_new.append(i)
print(str(lis_1_new))
print(str(lis_2_new))