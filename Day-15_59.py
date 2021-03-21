N = int(input("请输入数字："))
X = 0 
for i in range(1,N+1):
    X = i/(i+1) + X
print(X)
