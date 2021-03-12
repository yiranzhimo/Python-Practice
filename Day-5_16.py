nums = input("请输入 nums：").split(",")
nums = list(map(int,nums))
lis = list()
for item in nums:
    if item % 2 != 0:
        lis.append(item**2)
print(lis)

#运用 map 函数把 list 中国的字符串转换为 int
