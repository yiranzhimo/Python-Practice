def even(i):
    return i%2 ==0

def squ(i):
    return i*i

lis = [1,2,3,4,5,6,7,8,9,10]
print(list(map(squ,filter(even,lis) )))
#filter(function, iterable)，function -- 判断函数，iterable -- 可迭代对象。