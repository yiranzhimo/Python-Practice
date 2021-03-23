n = int(input("请输入数字："))
lis = list()
j = 0
if n == 0:
    print(j)
if n == 1:
    j = j + 1
    print(j)
i = 1
if n > 1:
    lis.append(0)
    lis.append(1)
    while i < n:
        i = i + 1
        j = lis[i-1]+lis[i-2]
        lis.append(j)
    print(lis)