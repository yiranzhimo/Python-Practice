lines = list()
lis = list()
while True:
    try:
        lines.append(input())
    except:
        break
#多行输入
for i in range(0,len(lines)):
    lis.append(tuple(lines[i].split(",")))
print(sorted(lis))

