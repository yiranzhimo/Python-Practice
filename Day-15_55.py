import re
str = input("请输入字符串：")
str_new = re.findall(r'(\d)\s\w*',str)
print(str_new)
#这个匹配比较模糊