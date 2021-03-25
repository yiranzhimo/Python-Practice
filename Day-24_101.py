words = list(input("请输入字符："))
lis_new = list()
for i in words:
    if i not in lis_new:
        lis_new.append(i)
for i in lis_new:
    num_i = words.count(i)
    print(i,num_i)