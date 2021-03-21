import re
str = input("请输入字符串：")
str_new = re.findall(r'(\w*)@',str)
print("".join(str_new))
#()可以表示匹配的范围