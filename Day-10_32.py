def test():
    dic = dict() 
    for i in range(1,21):
        dic[i]=i*i
    return dic.keys()
print(test())
#此时不需要定义参数