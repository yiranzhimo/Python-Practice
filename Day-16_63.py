n = int(input("请输入数字："))
lis = list()
for i in range(0,n+1):
    if i % 2 == 0:
        lis.append(str(i))
print(",".join(lis))