nums = input("请输入二进制数字：").split(",")
lis = list()
for item in nums:
    item_new = int(item,2)
    if item_new % 5 == 0:
        print(item)
