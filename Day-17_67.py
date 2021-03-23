def search(lis,item):
    if item not in lis:
        return None
    if item in lis:
        return lis.index(item)
lis = [1,2,3,4,5]
print(search(lis,3))