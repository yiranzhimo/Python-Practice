import re
word = input("请输入字符串：")
words = re.split(r" ",word)
#re.split 可以按照空格划分，而 str.split 直接全部切割
lis = list()
for item in words:
    if item not in lis:
        lis.append(item)
for item in sorted(lis):
    print(item,":",word.count(item))



