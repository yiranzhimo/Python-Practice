def test():
    lis = list() 
    for i in range(1,21):
        lis.append(i*i)
    return tuple(lis)
print(test())
