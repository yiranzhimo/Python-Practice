import re
word = input("请输入 words:")
result = ' '.join(re.findall(r'[A-Za-z]', word)).split()
list(result)
i = 0 
j = 0
for item in result:
    if item.islower() is True:
        i = i + 1
    else:
        j = j + 1
print("UPPER CASE ",j)
print("LOWER CASE ",i)

#使用了 re 模块的 findall 函数找到字母。