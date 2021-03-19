def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return lis[-5:]
print(test())
#此时不需要定义参数