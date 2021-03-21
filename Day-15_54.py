import re
str = input("请输入字符串：")
str_new = re.findall(r'\w*@(\w*).',str)
print("".join(str_new))