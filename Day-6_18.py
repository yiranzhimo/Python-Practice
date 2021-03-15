import re
passwords = input("请输入密码：").split(",")
for item in passwords:
    i = 0
    j = 0
    l = 0
    m = 0
    for word in item:
        if re.match(r"\d",word):
            i = i + 1
            #数字计数
        elif re.match("[a-z]",word):
            j = j + 1
        elif re.match("[A-Z]",word):
            l = l + 1
        elif re.match("[$#@]",word):
            m = m + 1
                
    
    if i >=1 and j >=1 and l >= 1 and m >=1 and len(item) in range(6,13):
        print(item)